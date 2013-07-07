from database.models import Author, Text, Section
from database import Session
from database.utilities import get_or_create
from prepare import parse_perseus, parse_xml
from generate import generate_ngrams

def load(file_path):
    if not file_path.endswith('xml'):
        print('Not an XML file:' + file_path)
        pass
    if file_path.endswith('DIY.xml'):
        author, title, sections = parse_xml(open(file_path))
    else:
        author, title, sections = parse_perseus(open(file_path),'div1')
    session = Session()
    a = get_or_create(session, Author, name=author)
    t = get_or_create(session, Text, name=title, author=a.id)
    session.commit()
    section_count = 1
    for sec in sections:
        temp_section = get_or_create(session, Section, source_text=t.id, number=section_count, content=sec)
        temp_section.ngrams = generate_ngrams(temp_section.content)
        section_count = section_count + 1
    session.commit()
