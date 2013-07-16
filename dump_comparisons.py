from database import *
from database.models import *

session = Session()

text_one_sections = session.query(Comparison,Section,Text,Author).join(Section).join(Text).join(Author)

for a in text_one_sections:
    print(a.Comparison.cosine_similarity)

