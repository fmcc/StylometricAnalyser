from bs4 import BeautifulSoup as BS
from BetacodeConvertor.BetacodeConvertor import *
import sys
import re

file_path = sys.argv[1]
output_folder = sys.argv[2]

con = BetacodeConvertor() 

parsed_text = BS(open(file_path), 'xml')
author = 'New Testament'
def strip_tag(tag):
    for t in parsed_text.find_all(tag):
        t.extract()

strip_tag('castList')
strip_tag('speaker')
strip_tag('note')
strip_tag('bibl')
strip_tag('head')
strip_tag('header')
one = '<text><author>'
two = '</author><title>'
three = '</title><section>'
four = '</section></text>'
i = 1
for item in parsed_text.findAll('div1'):
    single_spaced = re.sub('\s+',' ', item.text)
    unicode_text = con.convert(single_spaced)[0]
    title = item['n']
    print(title)
    out_file_name = re.sub('\s+','', author + title + 'DIY.xml') 
    output = one + author + two + title + three + unicode_text + four
    with open(output_folder + out_file_name, 'w') as write_out:
        write_out.write(output)
    i = i + 1
