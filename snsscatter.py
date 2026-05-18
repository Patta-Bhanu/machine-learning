import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")

sns.scatterplot(x="sepal_length",
                y="petal_length",
                data=iris,
                hue="species")

plt.show()