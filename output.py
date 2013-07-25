from database import *
from database.models import *
from compare import *

def full_distance_matrix(session):
    text_sections = session.query(Section,Text,Author).join(Text).join(Author)
    labels = [(chunk.Author.name,chunk.Text.name,str(chunk.Section.number))for chunk in text_sections]
    data = []
    for sec1 in text_sections:
        temp_data_row = []
        for sec2 in text_sections:
            temp_data_row.append(1-compare_texts(session,sec1.Section,sec2.Section))
        data.append(temp_data_row)
    return labels, data
