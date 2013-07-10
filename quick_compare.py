from database import *
from database.models import *
from compare import *

import sys

text_one = sys.argv[1]
text_two = sys.argv[2]

session = Session()

text_one_sections = session.query(Section,Text).join(Text).filter_by(name=text_one)
text_two_sections = session.query(Section,Text).join(Text).filter_by(name=text_two)

for sec1 in text_one_sections:
    for sec2 in text_two_sections:
        print(sec1.Text.name + " " + str(sec1.Section.number) + " " + str(compare_texts(session,sec1.Section,sec2.Section)) + " " + sec2.Text.name + " " + str(sec2.Section.number))
