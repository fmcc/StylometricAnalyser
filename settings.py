import os

DB_PATH = os.getcwd() + '/database/greek_texts.db'

DB_LOGGING = False

NGRAM_WORDS = False

NGRAM_LENGTHS = {
        'MIN': 2, 
        'MAX': 11
        }

RESTRICT_VECTOR_SPACE = 100000
