# model_validator task here => (if age > 50) => patient needs to have an emergency number in the contact details

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("data inserted.")


patient_info = {'name': 'nitish', 'email': 'abc@icici.com', 'age': 28, 'weight': 74.6, 'married': 1, 'allergies':['mushroom', 'black-pepper', 'dust', 'bright-sunlight'],
                'contact_details': {'email':'xyz@hotmail.com', 'phone': '2353462', 'emergency': '9554372350'}}



patient1 = Patient(**patient_info) # validation -> type coercion


insert_patient_data(patient1)