from database import *
from database.models import *
from collections import Counter

session = Session()

all_sections = session.query(Section,Text).join(Text).filter_by(name='Elements')

all_ngrams = Counter()

for sect in all_sections:
    print(sect.Section.number)
    all_ngrams = all_ngrams + Counter(sect.Section.ngrams)

print(all_ngrams.most_common(1000))

