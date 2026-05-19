import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=sns.load_dataset('iris')
df.head()
sns.pairplot(data=df,height=2,hue="species",palette='viridis',diag_kind='kde',plot_kws={"edgecolor":"black"})
plt.show()