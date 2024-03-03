import streamlit as st
import pandas as pd
import skops.io as sio
import numpy as np

st.set_page_config(
    page_title='Indian Motorcyles',
    page_icon='🏍️'
)

st.title('🏍️ Indian Motorcycles')

imcs = pd.read_pickle('./data/bikes_v4.pkl')

imcs_brands = imcs['model'].unique()
selected_brand = st.selectbox('Select Car Brand', options=imcs_brands)
imc_filtered = imcs[imcs['model'] == selected_brand]
imc_year = st.slider('Select Year of Registration', min_value=1950, max_value=2024, value=2000, step=1)
imc_owner = st.selectbox('Select Owner Type', options=imc_filtered['owner'].unique())
imc_name = st.selectbox('Select Motorcycle Name', options=imc_filtered['name'].unique())
imc_km = st.number_input('Select Kilometer')
imc_mileage = st.selectbox('Select Mileage', options=imc_filtered[imc_filtered['name']==imc_name]['mileage(kmpl)'].unique())

if st.button('Predict Price'):
    pipe = sio.load('./models/indianbikemodel_pipeline.skops',trusted=True)
    price = pipe.predict(pd.DataFrame([[imc_year,imc_owner,imc_name, selected_brand, imc_km, imc_mileage]], columns=['model_year', 'owner', 'name', 'model', 'km_driven', 'mileage(kmpl)']))[0]
    st.balloons()
    st.success(f'The price will range between {np.ceil(((price)**2-(((price)**2)*0.2)))} to {np.ceil(((price)**2+(((price)**2)*0.2)))} INR')