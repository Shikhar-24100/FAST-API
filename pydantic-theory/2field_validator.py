# Field validator

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        
        return value.upper()
    
    @field_validator('age', mode = 'after') # mode->default->after
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("data inserted.")


patient_info = {'name': 'nitish', 'email': 'abc@icici.com', 'age': 21, 'weight': 74.6, 'married': 1, 'allergies':['mushroom', 'black-pepper', 'dust', 'bright-sunlight'],
                'contact_details': {'email':'xyz@hotmail.com', 'phone': '2353462'}}



patient1 = Patient(**patient_info) # validation -> type coercion


insert_patient_data(patient1)