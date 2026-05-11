from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter 
import numpy as np
import csv
plt.style.use('fivethirtyeight')
data=pd.read_csv("C:\\Users\\ADMIN\\Downloads\\sample_languages_data.csv")
lang_work=data['LanguagesWorkedWith']
language_counter=Counter()
for res in lang_work:
    language_counter.update(res.split(';'))

languages=[]
popularity=[]
for item in sorted(language_counter.items(), key=lambda x: x[1]):
    languages.append(item[0])
    popularity.append(item[1])

plt.barh(languages,popularity,)
plt.title('popular languages used')
plt.ylabel('programming language')
plt.xlabel('no of people used')
plt.legend()
plt.tight_layout()
#plt.grid()
plt.show()