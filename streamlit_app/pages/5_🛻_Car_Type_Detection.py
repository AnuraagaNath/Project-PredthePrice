import streamlit as st
# import skops.io as sio
# from PIL import Image
import pandas as pd
import numpy as np
from tensorflow.keras import models
import cv2

st.set_page_config(
    page_title='Car Type Detection',
    page_icon='🛻'
)

st.title('🛻 Car Type Detection by Images')

images = {
    'Test Image 1': 'streamlit_app/images/image1.jpg',
    'Test Image 2': 'streamlit_app/images/image2.jpg',
    'Test Image 3': 'streamlit_app/images/image3.jpg',
    'Test Image 4': 'streamlit_app/images/image4.jpg',
    'Test Image 5': 'streamlit_app/images/image5.jpg',
    'Test Image 6': 'streamlit_app/images/image6.jpg',
    'Test Image 7': 'streamlit_app/images/image7.jpg',
    'Test Image 8': 'streamlit_app/images/image8.jpg',
    'Test Image 9': 'streamlit_app/images/image9.jpg',
    'Test Image 10': 'streamlit_app/images/image10.jpg',
    'Test Image 11': 'streamlit_app/images/image11.jpg',
    'Test Image 12': 'streamlit_app/images/image12.jpg',
    'Test Image 13': 'streamlit_app/images/image13.jpg',
    'Test Image 14': 'streamlit_app/images/image14.jpg',
    'Test Image 15': 'streamlit_app/images/image15.jpg',
    'Test Image 16': 'streamlit_app/images/image16.jpg',
    'Test Image 17': 'streamlit_app/images/image17.jpg',
    'Test Image 18': 'streamlit_app/images/image18.jpg',
    
}

selected_image = st.selectbox('Choose an image to test its type:', list(images.keys()))

filepath = images[selected_image]

st.image(filepath, width=300)

# model = sio.load('streamlit_app/models/car_detection_model_svc_balanced.skops',trusted=True)
model = models.load_model('streamlit_app/models/predtheprice_cnn.keras')

def imgtoarr(path):
    img = cv2.imread(path, 0)
    img = cv2.resize(img, (64, 64))
    img_array = np.expand_dims(img, axis=-1)
    return img_array, img_array.reshape(1, 64, 64, 1)

if st.button('Predict Car Type'):

    # image = Image.open(filepath).convert("L")
    # resized_image = image.resize((36,36), Image.ADAPTIVE)
    # pixel_values = np.array(resized_image)
    # normalized_pixel_values = (pixel_values).reshape(-1) / 255
    # columns = [f'pixel_{i}' for i in range(1296)]
    # ndf = pd.DataFrame([normalized_pixel_values], columns=columns)
    _, test_image = imgtoarr(filepath)
    # pred = model.predict_proba(ndf)[0]
    pred = model.predict(test_image)[0]
    hatchback = pred[0]
    pickup = pred[1]
    suv = pred[2]
    sedan = pred[3]
    st.balloons()
    st.text(f'Hatchback: {round(hatchback*100, 2)}%')
    st.progress(int(hatchback*100))
    st.text(f'Pickup: {round(pickup*100, 2)}%')
    st.progress(int(pickup*100))
    st.text(f'SUV: {round(suv*100, 2)}%')
    st.progress(int(suv*100))
    st.text(f'Sedan: {round(sedan*100, 2)}%')
    st.progress(int(sedan*100))




st.subheader('Citation of the Image data used: Boonsirisumpun, Narong; surinta, olarik (2021), “Vehicle Type Image Dataset (Version 2): VTID2”, Mendeley Data, V2, doi: 10.17632/htsngg9tpc.2')