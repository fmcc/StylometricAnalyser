import networkx as nx
import numpy as np
import string
import json 
import sys

input_json_file = sys.argv[1] 
output_file = sys.argv[2] 

with open(input_json_file, 'r') as json_in:
    text_data = json.loads(json_in.read())

labels = [item[0][0]+item[1][0]+item[2] for item in text_data['labels']]

dt = [('len', float)]

float_array = [[round(item,15)*100 for item in sub_array] for sub_array in text_data['data']]

data_array = np.array(float_array)    
data_array = data_array.view(dt)

G = nx.from_numpy_matrix(data_array)

labels = dict(zip(G.nodes(),labels))
G = nx.relabel_nodes(G, labels)    

G = nx.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color='black', width="0.5")

G.draw(output_file, format='png', prog='neato')
