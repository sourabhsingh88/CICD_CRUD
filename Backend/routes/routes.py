from fastapi import APIRouter, Depends , HTTPException
from utils.database import get_db
from sqlalchemy.orm import Session
from schemas.users import    UserBase ,UserUpdate , UserResponse , LoginRequest
from models.users import UserModel
from utils.security import  hash_password , verify_password
router = APIRouter(prefix="/user" , tags= ["User Router"])




@router.get("/")
def health() :
    return {"Message" : "Status OK 200 "}


@router.get("/all")
def get_all( db : Session = Depends(get_db)) : 
    return db.query(UserModel).all() 


@router.post("/create" , response_model = UserResponse)
def create_user(user : UserBase , db : Session = Depends(get_db)) :

    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()

    if existing_user :

        raise HTTPException(status_code= 400 , detail="email already exist")

    data=user.model_dump()
    # .dict  converts python model into normal dictionary

    data["password"] = hash_password(user.password)
    # new_user = UserModel(**user.dict())
    new_user = UserModel(**data)


    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.delete("/{user_id}")
def delete_user_id(user_id : int , db : Session = Depends(get_db)) :
    user = db.query(UserModel).filter(UserModel.id == user_id ).first()
    if not user :
        raise HTTPException(status_code=404 , detail= "user not found")
    db.delete(user)
    db.commit()
    return{"Message" : "User Deleted Successfully "}


@router.delete("/email")
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

        raise HTTPException(status_code= 404 , detail="User not found")

    db_user.name = user.name 
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user
                    

@router.patch("/{email}") 
def patch_user(email : str , user : UserUpdate , db : Session = Depends(get_db) ):
    db_user = db.query(UserModel).filter(UserModel.email == email).first()
    if not db_user :
        raise HTTPException(status_code=404 , detail="User not found")

    
    update_data = user.model_dump(exclude_unset=True)

    for key , value in update_data.items() :
        setattr(db_user , key , value)
    db.commit()  
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login_user (user : LoginRequest , db : Session = Depends(get_db) ) :
    db_user =  db.query(UserModel).filter(UserModel.email == user.email).first()

    if not db_user :
        raise HTTPException(
            status_code= 404 , detail="invalid emailor password"
        )

    is_valid_password = verify_password(user.password , db_user.password)

    if not is_valid_password :
        raise HTTPException (status_code= 401 , detail ="invalid email or password ")

    return {"message" : " Login Successfull" ,
            "user" : {
                "id" : db_user.id ,
                "email" : db_user.email ,
                "name" : db_user.name
            }}