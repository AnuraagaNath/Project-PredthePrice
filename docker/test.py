import pandas as pd
import skops.io as sio 
from PIL import Image
import numpy as np


model = sio.load('models/car_detection_model_svc.skops',trusted=True)
image = Image.open('test/PHOTO_44.jpg').convert("L")
resized_image = image.resize((36,36), Image.ADAPTIVE)
pixel_values = np.array(resized_image)
normalized_pixel_values = (pixel_values).reshape(-1) / 255
columns = [f'pixel_{i}' for i in range(1296)]
ndf = pd.DataFrame([normalized_pixel_values], columns=columns)
pred = model.predict_proba(ndf)
hatchback = pred[0][0]*100
pickup = pred[0][1]*100
sedan = pred[0][2]*100
suv = pred[0][3]*100

print((hatchback, pickup, sedan, suv))