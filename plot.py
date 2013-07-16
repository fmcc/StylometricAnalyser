import matplotlib.pyplot as plt
import numpy as np
from database import *
from database.models import *
from compare import *
import sys

output_name = sys.argv[1]

session = Session()
text_one_sections = session.query(Section,Text,Author).join(Text).join(Author)
text_two_sections = session.query(Section,Text,Author).join(Text).join(Author)
column_labels = []
row_labels = []
data = []
for sec1 in text_one_sections:
    column_labels.append(sec1.Author.name + ' - ' + sec1.Text.name + ' - ' + str(sec1.Section.number))
    temp_data_row = []
    for sec2 in text_two_sections:
        row_labels.append(sec2.Author.name + ' - ' + sec2.Text.name + ' - ' + str(sec2.Section.number))
        temp_data_row.append(compare_texts(session,sec1.Section,sec2.Section))
    data.append(temp_data_row)
np_data = np.array(data)

fig, ax = plt.subplots()
fig.set_size_inches(20,20)
heatmap = ax.pcolor(np_data, cmap=plt.cm.binary)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()
ax.set_yticks(np.arange(np_data.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(np_data.shape[1])+0.5, minor=False)
ax.set_xticklabels(row_labels, minor=False, size='x-small')
ax.set_yticklabels(column_labels, minor=False)
plt.xticks(rotation=90)
ax.grid(False)
plt.savefig(output_name)
