from database import *
from database.models import *
from database.utilities import get_or_create
from settings import DB_PATH
import os

if os.path.exists(DB_PATH):
    print('Database already exists')
else:
    Base.metadata.create_all(engine)
    session = Session()
    get_or_create(session, VectorSpace, space=set())
    session.commit()
