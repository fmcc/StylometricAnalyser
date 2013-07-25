import csv
import sys
import os
from compare import cosine_distance

dir_path = sys.argv[1]

def keep_comparison(comp):
    to_remove = ['Herodotus','Xenophon','New Testament','Euclid','Athenian Constitution']
    if comp['auth1'] in to_remove\
            or comp['auth2'] in to_remove\
            or comp['text1'] in to_remove\
            or comp['text2'] in to_remove\
            or (comp['auth1'],comp['text1'],comp['section1']) == (comp['auth2'],comp['text2'],comp['section2']):
        return False
    else:
        return True


def find_difference(comparisons):
    same = [float(comp['cossim']) for comp in comparisons if comp['auth1'] == comp['auth2']]
    diff = [float(comp['cossim']) for comp in comparisons if comp['auth1'] != comp['auth2']]
    same_average = sum(same)/len(same)
    diff_average = sum(diff)/len(diff)
    difference = same_average - diff_average
    return difference, diff_average, same_average

def distance_matrix(comparisons):
    sections = set([(comp['auth1'],comp['text1'],comp['section1']) for comp in comparisons])
    similarities = [[1-float(comp['cossim']) for comp in comparisons if sec[0] == comp['auth1'] and sec[1] == comp['text1'] and sec[2] == comp['section1']] for sec in sections]
    print(sections)
    similarities.sort(key = len)
    return_array = []
    for sim in similarities:
        for s in sim:
            return_array.append(s)
    return sections, return_array
            

    

def process_csv(file_in):
    with open(file_in, 'r') as results:
        print(file_in)
        data = csv.reader(results, delimiter=',')
        comparisons = []
        for row in data:
            comparison = {}
            comparison['auth1'] = row[0]
            comparison['text1'] = row[1]
            comparison['section1'] = row[2]
            comparison['cossim'] = row[3]
            comparison['auth2'] = row[4]
            comparison['text2'] = row[5]
            comparison['section2'] = row[6]
            comparisons.append(comparison)
        to_keep = [ comp for comp in comparisons if keep_comparison(comp) ]
        return distance_matrix(to_keep)
top_value = 0
actual_file = ""

from Pycluster import *

for root, dirs, files in os.walk(dir_path):
    for f in files:
        sections, matrix = process_csv(root + '/' + f) 
        clusterids,error, nfound = kmedoids(matrix, nclusters=9, npass=20, initialid=None)
        clusters = {}
        for section, clusterid in zip(sections, clusterids):
            clusters.setdefault(clusterid, []).append(section)
        
        for c in clusters.items():
            print(str(c) + '\n\n\n')

        # if diff[2] > 0.9 and diff[0] > top_value:
        #    print(root + '/' + f)
         #   print(diff)
          #  top_value = diff[0]
           # actual_file = f

#print( actual_file + ' ' +str(top_value))
