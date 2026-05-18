from matplotlib import pyplot as plt
from collections import Counter 
import numpy as np
import csv
plt.style.use('fivethirtyeight')

with open("C:\\Users\\ADMIN\\Downloads\\sample_languages_data.csv") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    language_counter=Counter()
    
    row=next(csv_reader)
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages=[]
popularity=[]
for item in language_counter.items():
    languages.append(item[0])
    popularity.append(item[1])


plt.barh(languages,popularity)
plt.title('popular languages used')
plt.ylabel('programming language')
plt.xlabel('no of people used')
plt.legend()
plt.tight_layout()
#plt.grid()
plt.show()