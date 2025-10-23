from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional


class UserInput(BaseModel):

    sepal_length: Annotated[float, Field(..., gt=0.0, description="length of the sepal")]
    sepal_width: Annotated[float, Field(..., gt=0.0, description="width of the sepal")]
    petal_length: Annotated[float, Field(..., gt=0.0, description="length of the petal")]
    petal_width: Annotated[float, Field(..., gt=0.0, description="width of the petal")]