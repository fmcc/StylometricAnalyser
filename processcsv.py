import csv
import sys
import os
import re
import numpy as np
import matplotlib as mpl
import scipy.stats as stats
from compare import cosine_distance

mpl.use("pgf")
pgf_with_custom_preamble = {
    "font.family": "serif", # use serif/main font for text elements
    "pgf.rcfonts": False,   # don't setup fonts from rc parameters
    "pgf.preamble": [
         r"\usepackage{units}",         # load additional packages
         r"\usepackage{metalogo}",
         r"\setmainfont{EB Garamond}", # serif font via preamble
         ]
}
mpl.rcParams.update(pgf_with_custom_preamble)

import matplotlib.pyplot as plt
dir_path = sys.argv[1]
dest = sys.argv[2]

def generate_labels(file_name):
    label = re.sub('.csv$','',file_name).split('_')
    label[1] = int(label[1])-1
    if label[2] == '0':
        length = 'All n-grams'
    else:
        length = "Top " + label[2] + " n-grams"

    if len(label) == 4:
        title = "Word n-grams - Vector space = " + length
    else:
        title = "Character n-grams - Vector space = " + length
    if int(label[0]) == label[1]:
        x_label = label[0]
    else:
        x_label = label[0] + "-" + str(label[1])
    return title,x_label

def clear_unwanted(comp):
    if (comp['auth1'],comp['text1'],comp['section1']) == (comp['auth2'],comp['text2'],comp['section2'])\
    or (comp['text1'],comp['text2']) == ('Athenian Constitution','Athenian Constitution')\
    or (comp['text1'],comp['text2']) == ('Mechanica','Mechanica')\
    or (comp['text1'],comp['text2']) == ('Athenian Constitution','Mechanica')\
    or (comp['text1'],comp['text2']) == ('Mechanica','Athenian Constitution')\
    or (comp['text1'],comp['section1']) == ('Athenian Constitution','4')\
    or (comp['text2'],comp['section2']) == ('Athenian Constitution','4'):
        return False
    else:
        return True

def remove_pseudo_texts(comp):
    to_remove = ['Mechanica','Athenian Constitution']
    if comp['text1'] in to_remove\
    or comp['text2'] in to_remove:
        return False
    else:
        return True

def find_difference(raw_comparisons):
    comparisons = [comp for comp in raw_comparisons if clear_unwanted(comp)]
    no_pseudo_texts = [comp for comp in comparisons if remove_pseudo_texts(comp)]
    arist = [1-float(comp['cossim']) for comp in no_pseudo_texts\
            if comp['auth1'] == 'Aristotle'
            and comp['auth2'] == 'Aristotle']

    cons = [1-float(comp['cossim']) for comp in comparisons\
            if comp['text1'] == 'Athenian Constitution'\
            or comp['text2'] == 'Athenian Constitution'\
            and comp['text1'] != 'Mechanica'\
            and comp['text2'] != 'Mechanica'\
            and comp['auth1'] == 'Aristotle'
            and comp['auth2'] == 'Aristotle']

    mech = [1-float(comp['cossim']) for comp in comparisons\
            if comp['text1'] == 'Mechanica'\
            or comp['text2'] == 'Mechanica'\
            and comp['text1'] != 'Athenian Constitution'\
            and comp['text2'] != 'Athenian Constitution'\
            and comp['auth1'] == 'Aristotle'\
            and comp['auth2'] == 'Aristotle']
    
    same = [1-float(comp['cossim']) for comp in no_pseudo_texts\
            if comp['auth1'] == comp['auth2']]

    diff = [1-float(comp['cossim']) for comp in no_pseudo_texts\
            if comp['auth1'] != comp['auth2']]

    arist_std_dev = np.std(arist)
    arist_avg = sum(arist)/len(arist)
    if mech:
        mech_avg = sum(mech)/len(mech)
    else:
        mech_avg = 0 
    cons_avg = sum(cons)/len(cons)
    arist_border = arist_avg + 2*arist_std_dev

    same_std_dev = np.std(same)
    same_avg = sum(same)/len(same)
    diff_avg = sum(diff)/len(diff)
    same_border = same_avg + 2*same_std_dev
    return {'Arist': {'arist':arist_avg, 'mech':mech_avg,'cons':cons_avg,'border':arist_border},\
            'All': {'same':same_avg,'diff':diff_avg,'border':same_border}}

def process_csv(file_in):
    with open(file_in, 'r') as results:
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
        return find_difference(comparisons)

def sort_by_type(values):
    title_types = set([value[0] for value in values])
    output = []
    for title in title_types:
        sub_list = sorted([(value[1],value[2]) for value in values if value[0] == title], key=lambda value : value[0])
        output.append((title,sub_list))
    return sorted(output, key=lambda item : item[0])

def plot_deviation(values,destination):
    plot_no = len(values)
    fig, ax = plt.subplots(plot_no,1)
    fig.tight_layout()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=0.3)
    fig.set_size_inches(6.36,16.44)
    for a,v in zip(ax,values):
        content = v[1]
        a.set_xticklabels([value[0] for value in content], minor=False,rotation=90)
        a.set_ylim([0,1])
        a.set_title(v[0])
        a.locator_params(axis='x',tight=True, nbins=len(content)+1)
        #same, = a.plot([item[1]['All']['same'] for item in content])
        #diff, = a.plot([item[1]['All']['diff'] for item in content])
        #border, = a.plot([item[1]['All']['border'] for item in content])
        arist, = a.plot([item[1]['Arist']['arist'] for item in content])
        mech, = a.plot([item[1]['Arist']['mech'] for item in content])
        cons, = a.plot([item[1]['Arist']['cons'] for item in content])
        arist_border, = a.plot([item[1]['Arist']['border'] for item in content])
        for i, val in enumerate(content):
            if val[1]['All']['diff'] > val[1]['All']['border']\
            and val[1]['Arist']['mech'] > val[1]['Arist']['border']\
            and val[1]['Arist']['cons'] > val[1]['Arist']['border']:
                a.axvline(x=i,linewidth=1, color='y')
    #plt.figlegend([same,diff,std_dev],["Average of same author","Average of different author","2sigma of same"],loc=4)
    plt.savefig(destination)

values= []
for root, dirs, files in os.walk(dir_path):
    for f in files:
        labels = generate_labels(f)
          
        dev = process_csv(root + '/' + f)
        values.append(labels + (dev,))
plot_deviation(sort_by_type(values),dest)




