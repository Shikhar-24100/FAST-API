#type validation->non-repetition of logic and data validation->restraint on data
 

# step1->define a pydantic model -> to represent the ideal schema of the data
# (expected fields, types, validation contraint)


# step2->instantiate the model with raw input data (usually a dictionary or JSON-like structure)->pydantic object
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='name of the patient', description='give name of the patient in les tahnt 50 chars', examples=['shikhar shrivasta'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    # weight: float = Field(gt=0)
    weight: Annotated[float, Field(gt=0, strict=True)]
    # married: bool
    married: Annotated[bool, Field(default=None, description='Is the patient married')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]   #optional field
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("data inserted.")


patient_info = {'name': 'nitish', 'email': 'abc@mail.com', 'linkedin_url': 'https://linkedin.com/Shikhar', 'age': 21, 'weight': 74.6, 'married': 1, 'allergies':['mushroom', 'black-pepper', 'dust', 'bright-sunlight'],
                'contact_details': {'email':'xyz@hotmail.com', 'phone': '2353462'}}




patient1 = Patient(**patient_info)


insert_patient_data(patient1)