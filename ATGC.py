import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
train = pd.read_csv('/Users/Donel/Desktop/train.csv')

train_mean = train.matches.mean()

cut_train = train.loc[train['matches'] > train_mean, [  'pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]
train_grouped = train.groupby('pos').sum()[['A','C','T','G']]

fig, ax = plt.subplots(1, figsize=(16, 6))
x = np.arange(0, len(train_grouped.index))
plt.bar(x - 0.3, train_grouped['A'], width = 0.2, color = '#1D2F6F')
plt.bar(x - 0.1, train_grouped['T'], width = 0.2, color = '#8390FA')
plt.bar(x + 0.1, train_grouped['G'], width = 0.2, color = '#6EAF46')
plt.bar(x + 0.3, train_grouped['C'], width = 0.2, color = '#FAC748')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('Millions of copies')
plt.xticks(x, train_grouped.index)
plt.xlim(-0.5, 31)
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.2)
# title and legend
plt.title('Nucleotides', loc ='left')
plt.legend(['A','C','T','G'], loc='upper left', ncol = 4)
plt.show()
