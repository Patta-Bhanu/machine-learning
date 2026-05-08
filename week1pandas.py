#Answering 5 questions
"""
1.Survival rate by gender — what % of males vs females survived?
2.Average age by passenger class — how did age differ across 1st, 2nd, and 3rd class?
3.Most common embarkation point — which port did most passengers board from?
4.% of missing values per column — which columns have gaps in the data?
5.Passengers with fare above average — how many people paid more than the mean ticket price?"""
import numpy as np
import pandas as pd
df=pd.read_csv("C:\\Users\\ADMIN\\Downloads\\archive\\Titanic-Dataset.csv",index_col="PassengerId")
#1
surviver_gender=df.groupby("Sex")["Survived"].mean()*100
print(surviver_gender)
#2
avg_age=df.groupby("Pclass")["Age"].mean().round(2)
print(avg_age)
#3
embark_count=df["Embarked"].value_counts()
print(embark_count)
#4
missing_percent=df.isnull().mean()*100
print(missing_percent)
#5
avg_fare = df["Fare"].mean()
count = df[df["Fare"] > avg_fare].shape[0]
print(count)