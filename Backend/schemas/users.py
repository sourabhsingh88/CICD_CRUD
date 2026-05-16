from  pydantic import BaseModel  
from typing import Optional

class UserBase(BaseModel) :
    name : str
    email : str
    password :str
    

class LoginRequest(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

class UserUpdate(BaseModel)  :
    name : Optional[str] = None
    email : Optional[str] = None

 