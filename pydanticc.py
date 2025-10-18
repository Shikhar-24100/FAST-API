# step1->create data schema
from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("data inserted 🍪")


patient_info = {'name': 'nitish', 'age': 21, 'weight': 74.6, 'married': 1, 'allergies':['mushroom', 'black-pepper', 'dust', 'bright-sunlight'],
                'contact_details': {'email':'xyz@hotmail.com', 'phone': '2353462'}}


patient1 = Patient(**patient_info)


insert_patient_data(patient1)