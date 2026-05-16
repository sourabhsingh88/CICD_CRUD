from fastapi import FastAPI
from utils.database import Base , engine
from routes.routes import  router as user_router


app =  FastAPI(title="|| User Crud And CICD ||")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],  # allows OPTIONS
    allow_headers=["*"],
)


@app.on_event("startup")
def start() :
    Base.metadata.create_all(bind = engine)

@app.get("/") 
def health() :
    return {"message" : "🎉🎉 All ohk server started 🎉🍾"}

app.include_router(user_router)

