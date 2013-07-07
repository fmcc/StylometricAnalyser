from database.models import Author, Text, Section
from database import Session
from database.utilities import get_or_create
from prepare import parse_perseus
from generate import generate_ngrams

def load(file_path):
    author, title, sections = parse_perseus(open(file_path),'div1')
    session = Session()
    a = get_or_create(session, Author, name=author)
    t = get_or_create(session, Text, name=title, author=a.id)
    session.commit()
    section_count = 1
    for sec in sections:
        temp_section = get_or_create(session, Section, source_text=t.id, number=section_count, content=sec)
        generate_ngrams(session, temp_section)
        section_count = section_count + 1
    session.commit()
