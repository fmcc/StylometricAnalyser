from database.models import Author, Text, Section, SectionContent, SectionNgrams, GlobalNgrams
from database import Session
from log import log
from database.utilities import get_or_create
from prepare import parse_perseus, parse_xml
from generate import generate_ngrams
from update import update_global_counts, update_vector_space

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
    session.commit()
    t = get_or_create(session, Text, name=title, author=a.id)
    session.commit()
    global_ngrams = session.query(GlobalNgrams).first()
    section_count = 1
    log('Loading: ' + t.name)
    for sec in sections:
        temp_section = get_or_create(session, Section, source_text=t.id, number=section_count)
        log('Loading section ' + str(section_count))
        session.commit()
        temp_section_content = get_or_create(session, SectionContent, section = temp_section.id, content = sec)
        log('Creating ngrams of ' + str(section_count))
        temp_section_ngrams = get_or_create(session, SectionNgrams, section = temp_section.id, ngrams = generate_ngrams(temp_section_content.content))
        log('Updating global ngram counts.')
        update_global_counts(session, global_ngrams,temp_section_ngrams.ngrams)
        section_count = section_count + 1
    session.commit()
    update_vector_space(session, global_ngrams)
