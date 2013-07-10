from database import *
from database.models import *
from database.utilities import *
session = Session()
aye = session.query(Section).first()
naw = session.query(Section).filter_by(id=4).first()

test = get_or_create(session,Comparison,text_one=aye.id, text_two=naw.id)
session.commit()
print(test.id)
test.profile_length = 1
test.cosine_similarity = 0.98
session.commit()


