from PerseusConvertor import * 
import sys
import os

def convert_perseus(source, destination):
    for root, dirs, files in os.walk(source):
        for f in files:
            file_path = root + '/' + f
            author, title, text = parse_perseus(open(file_path),'div1')
            dest_path = destination + '/' + author + '/' + title
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            book_num = 1
            for book in text:
                book_path = dest_path + '/' + str(book_num)
                with open(book_path, 'w') as output_file:
                    output_file.write(book)
                book_num += 1

convert_perseus(sys.argv[1],sys.argv[2])
