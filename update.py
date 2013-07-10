from database import *
from database.models import *
from generate import generate_vector_space
from collections import Counter
from settings import RESTRICT_VECTOR_SPACE

def update_vector_space(session, ngrams):
    vector = session.query(VectorSpace).first()
    vector_set = generate_vector_space(ngrams, vector.space)
    print(len(vector_set))
    session.query(VectorSpace).filter_by(id=1).update({'space': vector_set})
    session.commit()

def update_global_ngrams(session, ngrams):
    global_ngrams = session.query(GlobalNgrams).first()
    global_ngrams.global_ngram_counts = global_ngrams.global_ngram_counts + Counter(ngrams)
    print(len(global_ngrams.global_ngram_counts)) 
    global_ngrams.top_ngram_counts = global_ngrams.global_ngram_counts.most_common(RESTRICT_VECTOR_SPACE)
    print(len(global_ngrams.top_ngram_counts)) 
    session.commit()

