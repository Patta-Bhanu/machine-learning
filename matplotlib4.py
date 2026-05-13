from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')
ids = [x for x in range(1,101)]
data=pd.read_csv("C:\\Users\\ADMIN\\Downloads\\archive\\Titanic-Dataset.csv")
ages = data['Age']

bins=[10,20,30,40,50,60]
plt.hist(ages,bins=bins,edgecolor='black',log=True)
median_age=31

plt.axvline(median_age,color='r')
plt.legend()

plt.title('ages of responents')
plt.xlabel('Age')
plt.ylabel('salary')

plt.tight_layout()
plt.show()