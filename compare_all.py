from database import *
from database.models import *
from compare import *
import sys

session = Session()

text_sections = session.query(Section,Text).join(Text).order_by(Text.id)
for sec1 in text_sections:
    for sec2 in text_sections:
        print(sec1.Text.name + " " + str(sec1.Section.number) + " " + str(compare_texts(session,sec1.Section,sec2.Section)) + " " + sec2.Text.name + " " + str(sec2.Section.number))
