import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset('exercise')
df.head()
mp = sns.PairGrid(df)

mp.map_diag(sns.histplot)

mp.map_offdiag(sns.scatterplot)

plt.show()