import streamlit as st
import pandas as pd
import skops.io as sio
from joblib import load

st.set_page_config(
    page_title='Luxury Cars',
    page_icon='🚗'
)
st.title('🚗 Foreign Luxury Cars')

fcars = pd.read_pickle('streamlit_app/data/german_car.pkl')

fcars_brands = fcars['brand'].unique()
selected_brand = st.selectbox('Select Car Brand', options=fcars_brands)
fcar_filtered = fcars[fcars['brand'] == selected_brand]
fcar_name = st.selectbox('Select Car Name', options=fcar_filtered['name'].unique())
fcar_vehicleType = st.selectbox('Select Vehicle Type', options=fcar_filtered[fcar_filtered['name']==fcar_name]['vehicleType'].unique())
fcar_yor = st.slider('Select Year of Registration', min_value=2000, max_value=2024, value=2010, step=1)
fcar_gearbox = st.selectbox('Select Gearbox', options=fcar_filtered[fcar_filtered['name']==fcar_name]['gearbox'].unique())
fcar_km = st.number_input('Select Kilometer')
fcar_fuel = st.selectbox('Select Fuel Type', options=fcar_filtered[fcar_filtered['name']==fcar_name]['fuelType'].unique())
fcar_rd = st.selectbox('Select Not Repaired Damage (0 for No and 1 for Yes)', options=fcar_filtered['notRepairedDamage'].unique())

if st.button('Predict Price'):
    pipe = load('streamlit_app/models/carmodel_compressed.joblib')
    price = pipe.predict(pd.DataFrame([[fcar_name, fcar_vehicleType, fcar_yor, fcar_gearbox, fcar_km, fcar_fuel, selected_brand, fcar_rd]], columns=fcars.columns[:-1]))[0]
    st.balloons()
    st.success(f'The price will range between {price-(price*0.2)} to {price+(price*0.2)} INR')