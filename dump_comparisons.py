from database import *
from database.models import *
from sqlalchemy.orm import aliased
import sys

file_path = sys.argv[1]

session = Session()
section_alias = aliased(Section, name='section_alias')
author_alias = aliased(Author, name='author_alias')
text_alias = aliased(Text, name='text_alias')

text_one_sections = session.query(Comparison,\
                                Section,\
                                section_alias,\
                                Author,\
                                author_alias,\
                                Text,\
                                text_alias\
                                )\
        .join(Section, Comparison.text_one==Section.id)\
        .join(Text, Section.source_text==Text.id)\
        .join(Author, Text.author==Author.id)\
        .join(section_alias, Comparison.text_two==section_alias.id)\
        .join(text_alias, section_alias.source_text==text_alias.id)\
        .join(author_alias, text_alias.author==author_alias.id)
 
output = ""

for item in text_one_sections:
    output = output + item.Author.name + ','\
            + item.Text.name + ','\
            + str(item.Section.number) + ','\
            + str(item.Comparison.cosine_similarity) + ','\
            + item.author_alias.name + ','\
            + item.text_alias.name + ','\
            + str(item.section_alias.number) + '\n'
            

with open(file_path, 'w') as out:
    out.write(output)

