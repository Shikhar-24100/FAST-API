import pickle
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "iris_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


MODEL_VERSION = '1.0.0'


def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])

    output = model.predict(input_df)[0]

    return output