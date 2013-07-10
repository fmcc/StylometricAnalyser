from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import *

Base = declarative_base()
engine = create_engine('sqlite:///' + DB_PATH, echo=DB_LOGGING)
Session = sessionmaker(bind=engine)
