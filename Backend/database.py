from sqlalchemy.orm import declarative_base  , sessionmaker
from sqlalchemy.engine import create_engine 
import os 
import time
from sqlalchemy.exc import OperationalError


DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL, future=True, pool_pre_ping=True)
        engine.connect()
        break
    except OperationalError:
        print("Database not ready, retrying...")
        time.sleep(2)
else:
    raise RuntimeError("Database not available")

# engine =  create_engine(DATABASE_URL , future= True , pool_pre_ping=True )

SessionLocal = sessionmaker(bind= engine , autocommit = False , autoflush=False)

Base =  declarative_base ()

def get_db() :
    db= SessionLocal()
    try :
        yield db 
    finally :
        db.close()
