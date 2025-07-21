import pickle
import numpy as np

def load_model(path="models/model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

def predict_sales(model, tv, radio, news):
    features = np.array([[tv, radio, news]])
    return model.predict(features)[0]
