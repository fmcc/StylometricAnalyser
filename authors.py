from database import *
from database.models import *
from compare import *
import sys
query = sys.argv[1]

session = Session()

if query == 'author':
    results = session.query(Text,Author).join(Author)
    for item in results:
        print(item.Author.name + " " + item.Text.name)
if query == 'text':
    results = session.query(Section, Text).join(Text)
    for item in results:
        print(item.Text.name + " " + str(item.Section.number))
else:
    print("Must be 'author' or 'text'.")
