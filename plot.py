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
    print(pos)
    authors = set([label[0] for label in axes_labels])
    authors_texts = {}
    for a in authors:
        authors_texts[a] = {item[1]:[] for item in axes_labels if item[0]==a}
   
    for label, p in zip(axes_labels,pos):
        authors_texts[label[0]][label[1]].append(p)
    
    colours = iter(plt.cm.rainbow(np.linspace(0, 1, len(authors))))
    for author in authors_texts:
        colour = next(colours)
        shapes = iter(['o','^','s','p','D'])
        for text in authors_texts[author]:
            shape = next(shapes)
            coords = authors_texts[author][text]
            x_coord = [item[0] for item in coords]
            y_coord = [item[1] for item in coords]
            plt.scatter(x_coord,y_coord,c=colour,marker=shape)

    plt.savefig(output_path)
