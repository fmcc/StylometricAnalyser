output_one = """
import os

DB_PATH = os.getcwd() + '/database/greek_texts.db'

LOGGING = True
DB_LOGGING = False

NGRAM_WORDS = False

NGRAM_LENGTHS = {
        'MIN': """
output_two = """, 
        'MAX': """
        
output_three = """
}

NO_SPACES = False

RESTRICT_VECTOR_SPACE = """

output_four = """

# If selected, texts will be divided according to their original top-level divisions (Books etc. 'div1' in Perseus's TEI XML
USE_ORIGINAL_DIVISIONS = False 

#If USE_ORIGINAL_DIVISIONS is False, the text will be divided into chunks the length defined here. If O the text will not be divided. 
DIVISION_LENGTH = 5000
"""

V_S = ['0','200','1000']

h = 1
for vs in V_S:
    for q in range(1,9):
        for i in range(1,9):
            j = i + q
            if j <= 9:
                file_name = str(h) + '_' + str(i) + '_' + str(j) + '_' + vs + '.py'
                print(file_name)
                h = h + 1
                with open('./test_settings/' + file_name, 'w') as out:
                    out.write(output_one + str(i) + output_two + str(j) + output_three + vs + output_four)
