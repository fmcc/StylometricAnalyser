from database import *
from database.models import *
from database.utilities import get_or_create
from settings import DB_PATH
from collections import Counter
import os

if os.path.exists(DB_PATH):
    print('Database already exists')
else:
    Base.metadata.create_all(engine)
    session = Session()
    get_or_create(session, VectorSpace, space=set())
    get_or_create(session, GlobalNgrams, global_ngram_counts=Counter(),top_ngram_counts=[])
    session.commit()
