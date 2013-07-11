from collections import Counter
from settings import RESTRICT_VECTOR_SPACE
from database.models import GlobalVersion, VectorSpace 
from log import log

def update_global_counts(session, global_ngrams, ngrams):
    global_ngrams.counts = global_ngrams.counts + Counter(ngrams)
    session.commit()
    return

def update_vector_space(session, global_ngrams):
    vector_space = session.query(VectorSpace).first()
    global_version = session.query(GlobalVersion).first()
    global_version.version = global_version.version + 1
    session.commit()
    if RESTRICT_VECTOR_SPACE:
        log('Updating restricted vector space: Length = ' + str(RESTRICT_VECTOR_SPACE))
        vector_space.space = set(global_ngrams.counts.most_common(RESTRICT_VECTOR_SPACE))
        session.commit()
        return
    all_ngrams = global_ngrams.counts.keys()
    log('Updating vector space: Length = ' + str(len(all_ngrams)))
    vector_space.space = set(all_ngrams)
    session.commit()
    return
