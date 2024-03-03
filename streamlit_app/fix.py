from joblib import dump, load
import skops.io as sio

# Save the model with compression
dump(sio.load('models/carmodel.skops', trusted=True), 'models/carmodel_compressed.joblib', compress=3)


