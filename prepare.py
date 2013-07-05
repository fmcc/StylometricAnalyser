from bs4 import BeautifulSoup as BS
from BetacodeConvertor.BetacodeConvertor import *
import re

"""
This function will take in a Perseus XML text and output a list of the text of the chapters
"""
def parse_perseus(xml_text, unit):
    parsed_text = BS(xml_text, 'xml')
    con = BetacodeConvertor() 
    author = parsed_text.author.text
    def create_title(parsed):
        text_info = parsed.titleStmt
        title = " ".join([t.text for t in text_info('title')])
        title = re.sub('Machine readable text|\.|\(Greek\)','', title).strip()
        return title
    title = create_title(parsed_text)
    def strip_tag(tag):
        for t in parsed_text.find_all(tag):
            t.extract()
    strip_tag('note')
    strip_tag('bibl')
    strip_tag('head')
    books = []
    for item in parsed_text.find_all(unit):
        single_spaced = re.sub('\s+',' ', item.text)
        unicode_passage = con.convert(single_spaced)[0]
        books.append(unicode_passage)

    return author, title, books
