
import os

DB_PATH = os.getcwd() + '/database/greek_texts.db'

LOGGING = True
DB_LOGGING = False

NGRAM_WORDS = False

NGRAM_LENGTHS = {
        'MIN': 1, 
        'MAX': 4
}

NO_SPACES = False

RESTRICT_VECTOR_SPACE = 0

# If selected, texts will be divided according to their original top-level divisions (Books etc. 'div1' in Perseus's TEI XML
USE_ORIGINAL_DIVISIONS = False 

#If USE_ORIGINAL_DIVISIONS is False, the text will be divided into chunks the length defined here. If O the text will not be divided. 
DIVISION_LENGTH = 5000
