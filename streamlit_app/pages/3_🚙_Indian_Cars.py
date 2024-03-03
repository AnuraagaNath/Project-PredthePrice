import streamlit as st
import pandas as pd
import skops.io as sio

st.set_page_config(
    page_title='Indian Cars',
    page_icon='🚙'
)
st.title('🚙 Indian Cars')

icars = pd.read_csv('/home/anuraaga/Documents/Projects/Project-PredthePrice/docker/data/indian_car.csv', index_col=0)

icars_brands = icars['company'].unique()
selected_brand = st.selectbox('Select Car Brand', options=icars_brands)
icar_filtered = icars[icars['company'] == selected_brand]
icar_name = st.selectbox('Select Car Name', options=icar_filtered['name'].unique())
icar_year = st.slider('Select Year of Registration', min_value=1950, max_value=2024, value=2000, step=1)
icar_km = st.number_input('Select Kilometer')
icar_fuel = st.selectbox('Select Fuel Type', options=icar_filtered[icar_filtered['name']==icar_name]['fuel_type'].unique())

if st.button('Predict Price'):
    pipe = sio.load('/home/anuraaga/Documents/Projects/Project-PredthePrice/docker/models/indiancarmodel_pipeline.skops',trusted=True)
    price = pipe.predict(pd.DataFrame([[icar_name, selected_brand, icar_year, icar_km, icar_fuel]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))[0]
    st.balloons()
    st.success(f'The price will range between {price-(price*0.2)} to {price+(price*0.2)} INR')