from database import *
from database.models import *
from compare import *
import sys

session = Session()

text_sections = session.query(Section,Text,Author).join(Text).order_by(Text.id).join(Author).filter_by(name=sys.argv[1])
for sec1 in text_sections:
    for sec2 in text_sections:
        print(compare_texts(session,sec1.Section,sec2.Section))
