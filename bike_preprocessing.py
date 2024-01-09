import pandas as pd
import numpy as np
import re

# the data is taken from https://www.kaggle.com/datasets/ropali/used-bike-price-in-india
df = pd.read_csv('bikes.csv')

# Get Bike and Model name
def getBikeName(name):
    '''Returns bike name from model_name column
    
    Keyword argument:
    name -- the model name from the series
    '''
    bikename = name.split()[:-1]
    return " ".join(bikename)

def getModelName(name):
    '''Returns model name from model_name column
    
    Keyword argument:
    name -- the model name from the series
    '''
    modelname = name.split()[0]
    return modelname

# Applying methods to get bike and model names seperately
df['name'] = df['model_name'].apply(getBikeName)
df['model'] = df['model_name'].apply(getModelName)

df.drop('model_name', axis=1, inplace=True)

# Cleaning the Kilometer driven column and Mileage column. Finally applying the methods to return a cleaned dataframe
def getKMdriven(kms):
    '''Returns kilometer value in integer format
    
    Keyword argument:
    kms -- kilometer string from the series
    '''
    try:
        if kms.startswith('Mileage'):
            km = int(kms.split()[1])
        elif kms.endswith('Kmpl'):
            km = int(kms[:2])
        else:
            km = int(kms.split()[0])
        return km
    except ValueError:
        km = kms.split()[1]
        if km == 'Km':
            return km
        else:
            return int(km[:2])

# Apply the getKMdriven method
df['km_driven'] = df['kms_driven'].apply(getKMdriven)


for index, row in df.iterrows():
    if row['km_driven'] == 'Km':
        df.drop(index, inplace=True)

# drop unnecessary columns
cldf = df.reset_index().drop(['kms_driven', 'location', 'power', 'index'], axis=1)

def cleanMileage(mileage):
    '''Returns mileage value in float format and Null in case of invalid value
    
    Keyword argument:
    mileage -- mileage string from series
    '''
    try:
        miles = re.sub('\n\n', '', str(mileage))
        mile = miles.strip()[:2]
        return float(mile)
    except ValueError:
        return np.nan

# applying methods and formatting columns in correct format
cldf['mileage(kmpl)'] = cldf['mileage'].apply(cleanMileage)
cldf.dropna(inplace=True)
data = cldf.drop('mileage', axis=1)
data['mileage(kmpl)'] = data['mileage(kmpl)'].astype(int)
data['km_driven'] = data['km_driven'].astype(int)