from database import Base 
from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy import  Integer ,String 

class UserModel(Base) :
    __tablename__ = "users"  

    id : Mapped[int] = mapped_column(Integer , primary_key = True , index = True)
    name : Mapped[str] = mapped_column(String(50) , index = True)
    email : Mapped[str] = mapped_column(String(50) , unique  =True , index =True)
   