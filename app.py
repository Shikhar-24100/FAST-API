from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import pickle

import pandas as pd


app = FastAPI()



with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)


class UserInput(BaseModel):

    sepal_length: Annotated[float, Field(..., gt=0.0, description="length of the sepal")]
    sepal_width: Annotated[float, Field(..., gt=0.0, description="width of the sepal")]
    petal_length: Annotated[float, Field(..., gt=0.0, description="length of the petal")]
    petal_width: Annotated[float, Field(..., gt=0.0, description="width of the petal")]



@app.post('/predict')
def predict_variety(data: UserInput):

    input_df = pd.DataFrame([{
        'sepal length': data.sepal_length,
        'sepal width': data.sepal_width,
        'petal length': data.petal_length,
        'petal width': data.petal_width
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'predicted_category': prediction})



