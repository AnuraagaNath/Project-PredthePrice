
# import packages
import pandas as pd
import re
import string
from preprocessor.functions import translateClass


# read csv file for car data

# download the data from https://data.world/data-society/used-cars-data
df = pd.read_csv('autos.csv', encoding_errors='ignore')

# - dateCrawled : when this ad was first crawled, all field-values are taken from this date
# - name : "name" of the car
# - seller : private or dealer
# - offerType
# - price : the price on the ad to sell the car
# - abtest
# - vehicleType
# - yearOfRegistration : at which year the car was first registered
# - gearbox
# - powerPS : power of the car in PS
# - model
# - kilometer : how many kilometers the car has driven
# - monthOfRegistration : at which month the car was first registered
# - fuelType
# - brand
# - notRepairedDamage : if the car has a damage which is not repaired yet
# - dateCreated : the date for which the ad at ebay was created
# - nrOfPictures : number of pictures in the ad
# - postalCode
# - lastSeenOnline : when the crawler saw this ad last online


def clean_name(name):
    '''Returns cleaned name of the car

    Keyword argument:
    name -- name of the car
    '''
    modelname = name.replace('_', ' ')
    modelname = modelname.strip()
    return modelname

df['name'] = df['name'].apply(clean_name)




# find if any character in object dtype column contains special characters
cols = df.columns[df.dtypes == object]
cols_with_punctuations = []
for col in cols:
    any_punctuation = any(char in string.punctuation for text in df[col].dropna() for char in text)
    if any_punctuation:
        cols_with_punctuations.append(col)


# substitute those characters with blank character
for col in cols_with_punctuations:
    df[col] = df[col].apply(lambda text: re.sub(f'[{re.escape(string.punctuation)}]', '', str(text)) if pd.notnull(text) else text)


df['name'] = df['name'].str.strip()
cldf = df[df['name']!='']

# creating new dataframe for backup
cldf2 = cldf.copy()
cldf2['brand']=cldf2['brand'].apply(lambda x: x.capitalize())

# special treatment to a datapoint
cldf2.at[1,'name'].split()[0] != cldf2.at[371495, 'brand']


# get null model value rows 
nan_model_rows = cldf2[cldf2['model'].isna()]


# formatting the name column as brand name + car model name
for index, row in nan_model_rows.iterrows():
    if cldf2.at[index,'name'].split()[0] != cldf2.at[index, 'brand']:
        cldf2.at[index,'name'] = row['brand'] + " " + row['name']


newdata = cldf2.drop(['dateCrawled', 'dateCreated', 'lastSeen', 'postalCode', 'nrOfPictures', 'model', 'powerPS', 'offerType', 'seller'], axis=1)


newdata['name'] = newdata['name'].apply(lambda x: " ".join(x.split()[:3]))


vehicleTypeUnique = newdata['vehicleType'].dropna().unique()


cldf3 = newdata.drop_duplicates().reset_index().drop('index', axis=1)


cldf3['vehicleType'].fillna('andere', inplace=True)

rename = translateClass(vehicleTypeUnique)
cldf3['vehicleType'] = cldf3['vehicleType'].replace(rename)
cldf3['vehicleType'] = cldf3['vehicleType'].str.capitalize()
cldf3['vehicleType'].replace({'Small car':'Compact'}, inplace=True)


# converting price using current price convertion rate between euro and inr
cldf3['price(inr)'] = cldf3['price'].apply(lambda x: x*90)
cldf3.drop('price', inplace=True, axis=1)

# cleaning gearbox column
cldf3['gearbox'].fillna(cldf3['gearbox'].mode()[0], inplace=True)
cldf3['gearbox'].replace({'manuell':'manual', 'automatik':'automatic'}, inplace=True)
cldf3['gearbox'].value_counts()
cldf3['gearbox'] = cldf3['gearbox'].str.capitalize()


# cleaning fueltype column
cldf3['fuelType'].fillna('andere', inplace=True)
uniqueFuelType = cldf3['fuelType'].unique()
replaceFuelType = translateClass(uniquevalues=uniqueFuelType)
cldf3['fuelType'].replace(replaceFuelType, inplace=True)
cldf3['fuelType'].value_counts()
cldf3['fuelType'] = cldf3['fuelType'].str.capitalize()
cldf3['fuelType'].replace({'Electro':'Electric'}, inplace=True)

# cleaning notRepairedDamage column
cldf3['notRepairedDamage'].fillna('nein', inplace=True)
cldf3['notRepairedDamage'].replace({'nein':False, 'ja':True}, inplace=True)