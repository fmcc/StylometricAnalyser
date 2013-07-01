from PerseusConvertor import * 
import sys

author, title, text = parse_perseus(open(sys.argv[1]),'div1')

print(author)
print(title)

lengths = [len(passage) for passage in text]

print(text)
