import streamlit as st
import skops.io as sio
from PIL import Image
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Car Type Detection',
    page_icon='🛻'
)

st.title('🛻 Car Type Detection by Images')

images = {
    'Test Image 1': '/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/Hatchback/PHOTO_3.jpg',
    'Test Image 2': '/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/Hatchback/PHOTO_9.jpg',
    'Test Image 3': '/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/Pickup/PHOTO_6.jpg',
    'Test Image 4': '/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/Pickup/PHOTO_24.jpg',
    'Test Image 5': '/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/Seden/PHOTO_5.jpg',
    'Test Image 6': '/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/Seden/PHOTO_12.jpg',
    'Test Image 7':'/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/SUV/PHOTO_8.jpg',
    'Test Image 8':'/home/anuraaga/Documents/Projects/Project-PredthePrice/train_image/test_image/SUV/PHOTO_14.jpg'
    
}

selected_image = st.selectbox('Choose an image to test its type:', list(images.keys()))

filepath = images[selected_image]

st.image(filepath, width=300)

model = sio.load('/home/anuraaga/Documents/Projects/Project-PredthePrice/docker/models/car_detection_model_svc_balanced.skops',trusted=True)

if st.button('Predict Car Type'):

    image = Image.open(filepath).convert("L")
    resized_image = image.resize((36,36), Image.ADAPTIVE)
    pixel_values = np.array(resized_image)
    normalized_pixel_values = (pixel_values).reshape(-1) / 255
    columns = [f'pixel_{i}' for i in range(1296)]
    ndf = pd.DataFrame([normalized_pixel_values], columns=columns)
    pred = model.predict_proba(ndf)[0]
    hatchback = pred[0]
    pickup = pred[1]
    sedan = pred[2]
    suv = pred[3]
    st.text(f'Hatchback: {round(hatchback*100, 2)}%')
    st.progress(hatchback)
    st.text(f'Pickup: {round(pickup*100, 2)}%')
    st.progress(pickup)
    st.text(f'Sedan: {round(sedan*100, 2)}%')
    st.progress(sedan)
    st.text(f'SUV: {round(suv*100, 2)}%')
    st.progress(suv)