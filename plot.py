import matplotlib.pyplot as plt
import numpy as np
from sklearn import manifold
from output import full_distance_matrix

def matrix_heatmap(session, output_path):
    axes_labels, data_matrix = full_distance_matrix(session)
    axes_labels = [label[0] + ' '+ label[1] + ' ' + label[2] for label in axes_labels]
    np_matrix = np.array(data_matrix)
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(np_matrix, cmap=plt.cm.summer)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.set_yticks(np.arange(np_matrix.shape[0])+0.5, minor=False)
    ax.set_xticks(np.arange(np_matrix.shape[1])+0.5, minor=False)
    ax.set_xticklabels(axes_labels, minor=False, size='x-small')
    ax.set_yticklabels(axes_labels, minor=False, size='x-small')
    plt.xticks(rotation=90)
    ax.grid(False)
    plt.savefig(output_path)

def mds_plot(session, output_path):
    axes_labels, data_matrix = full_distance_matrix(session)
    np_matrix = np.array(data_matrix)
    mds = manifold.MDS(n_components=2, max_iter=3000, dissimilarity='precomputed')
    pos = mds.fit(np_matrix).embedding_
    pos = [[item[0],item[1]] for item in pos]
    authors = set([label[0] for label in axes_labels])
    authors_texts = {}
    fig, ax = plt.subplots()
    fig.set_size_inches(10,10)
    for a in authors:
        authors_texts[a] = {item[1]:[] for item in axes_labels if item[0]==a}
   
    for label, p in zip(axes_labels,pos):
        authors_texts[label[0]][label[1]].append(p)
    
    colours = iter(['r','g','b','y','m','c'])
    for author in authors_texts:
        colour = next(colours)
        shapes = iter(['o','^','s','p','D','x'])
        for text in authors_texts[author]:
            shape = next(shapes)
            coords = authors_texts[author][text]
            x_coord = [item[0] for item in coords]
            y_coord = [item[1] for item in coords]
            ax.scatter(x_coord,y_coord,c=colour,marker=shape, label = author + ' - ' + text)
    ax.legend(loc=2,fontsize=8,scatterpoints=1)
    plt.savefig(output_path)
