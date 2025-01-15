# import random
from pydantic import BaseModel, EmailStr

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        
# class UserCreate(BaseModel):
#     user_id : int
#     name: str
#     email: EmailStr
#     vector: list[float]  # Assuming vector is a list of float
        

    # def to_dict(self):
    #     return {"user_id": self.user_id, "name": self.name, "email": self.email}