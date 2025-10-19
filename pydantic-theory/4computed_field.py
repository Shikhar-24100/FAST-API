# computed field: eg-> bmi which is dynamically caculated in the given example using user inputs(weight and height)

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict



class Patient(BaseModel):

    name: str 
    email: EmailStr
    age: int
    weight: float  #kg
    height: float #mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight/self.height**2), 2)
        return bmi



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('BMI:',patient.bmi)
    print("data inserted.")


patient_info = {'name': 'nitish', 'email': 'abc@icici.com', 'age': 28, 'weight': 74.6, 'height':1.72, 'married': 1, 'allergies':['mushroom', 'black-pepper', 'dust', 'bright-sunlight'],
                'contact_details': {'email':'xyz@hotmail.com', 'phone': '2353462', 'emergency': '9554372350'}}



patient1 = Patient(**patient_info) # validation -> type coercion


insert_patient_data(patient1)