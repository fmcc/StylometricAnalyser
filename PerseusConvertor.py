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
    titles = [t.text for t in parsed_text.find_all('title')]
    titles.remove('Machine readable text')
    def strip_tag(tag):
        for t in parsed_text.find_all(tag):
            t.extract()

    strip_tag('note')
    strip_tag('head')

    books = []

    for item in parsed_text.find_all(unit):
        unicode_passage = con.convert(item.text)[0]
        single_spaced = re.sub('\s+',' ', unicode_passage)
        books.append(single_spaced)

    return author, titles, books
