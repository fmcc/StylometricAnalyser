from database import *
from database.models import *
from generate import generate_vector_space

def update_vector_space(session, ngrams):
    vector = session.query(VectorSpace).first()
    vector_set = generate_vector_space(ngrams, vector.space)
    print(len(vector_set))
    session.query(VectorSpace).filter_by(id=1).update({'space': vector_set})
    session.commit()
