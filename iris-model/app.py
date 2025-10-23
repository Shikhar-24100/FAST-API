from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
import json
# from pydantic import BaseModel, Field, computed_field
# from typing import Annotated, Literal, Optional
from schema.user_input import UserInput
from model.predict import predict_output, MODEL_VERSION




app = FastAPI()









# huma readable
@app.get('/')
def home():
    return {'message': 'Iris category prediction API'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status' : 'OK',
        'version': MODEL_VERSION
    }


@app.post('/predict')
def predict_variety(data: UserInput):

    user_input = {
    'sepal length (cm)': data.sepal_length,
    'sepal width (cm)': data.sepal_width,
    'petal length (cm)': data.petal_length,
    'petal width (cm)': data.petal_width
    }

    prediction = predict_output(user_input)
    prediction = int(prediction)  # or str(prediction)
    # return {"predicted_category": prediction}
    # prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'predicted_category': prediction})





