from database import *
from database.models import *
from database.utilities import get_or_create
from settings import DB_PATH, NGRAM_LENGTHS, RESTRICT_VECTOR_SPACE
from collections import Counter
import os

if os.path.exists(DB_PATH):
    print('Database already exists')
else:
    Base.metadata.create_all(engine)
    session = Session()
    get_or_create(session, VectorSpace, space=set())
    get_or_create(session, GlobalNgrams, counts=Counter())
    get_or_create(session, GlobalVersion)
    session.commit()
    print(str(NGRAM_LENGTHS['MIN']) + ' - ' + str(NGRAM_LENGTHS['MAX']) + ' - ' + str(RESTRICT_VECTOR_SPACE))
