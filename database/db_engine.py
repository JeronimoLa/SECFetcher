from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config import get_configuration

config = get_configuration()

DATABASE_URL = config["db_url"]

engine = create_engine(DATABASE_URL, echo=True)
session = Session(engine)


def get_db():
    """ create's db session per request """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



