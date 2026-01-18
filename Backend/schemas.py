from  pydantic import BaseModel  
from typing import Optional

class UserBase(BaseModel) :
    name : str
    email : str
    

    
class UserUpdate(BaseModel)  :
    name : Optional[str] = None
    email : Optional[str] = None

 