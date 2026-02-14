from fastapi import APIRouter, Depends , HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas import    UserBase ,UserUpdate
from model import UserModel

router = APIRouter(prefix="/user" , tags= ["User Router"])




@router.get("/")
def health() :
    return {"Message" : "Status OK 200 "}


@router.get("/all")
def get_all( db : Session = Depends(get_db)) : 
    return db.query(UserModel).all() 


@router.post("/create") 
def create_user(user : UserBase , db : Session = Depends(get_db)) :
    data=user.dict()
    
    # new_user = UserModel(**user.dict())
    new_user = UserModel(**data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 



@router.delete("/id/{user_id}")
def delete_user_id(user_id : int , db : Session = Depends(get_db)) :
    user = db.query(UserModel).filter(UserModel.id == user_id ).first()
    if not user :
        raise HTTPException(status_code=404 , detail= "user not found")
    db.delete(user)
    db.commit()
    return{"Message" : "User Deleted Successfully "}


@router.delete("/email/{email}")
def delete_by_email(email : str , db : Session = Depends(get_db)) :
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user :
        raise HTTPException(status_code=404 , detail="User Not found with given email")
    db.delete(user)
    db.commit()
    return {"message" : "User deleted Successfully"}


@router.put("/{email}")
def update_by_email(email :str , user : UserBase , db : Session = Depends(get_db)) :
    db_user = db.query(UserModel).filter(UserModel.email == email).first()
    if not db_user :
        raise HTTPException(status_code= 404 , detail="Usr not found")
    db_user.name = user.name 
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user
                    

@router.patch("/{email}") 
def update_user(email : str , user : UserUpdate , db : Session = Depends(get_db) ):
    db_user = db.query(UserModel).filter(UserModel.email == email).first()
    if not db_user :
        raise HTTPException(status_code=404 , detail="User not found")

    update_data = user.dict(exclude_unset=True)
    for key , value in update_data.items() :
        setattr(db_user , key , value)
    db.commit()  
    db.refresh(db_user)
    return db_user


