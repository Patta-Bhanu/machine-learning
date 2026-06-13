import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# -------------------------------
# Load Train and Test Datasets
# -------------------------------
df_train = pd.read_csv(r"C:\Users\ADMIN\Downloads\train.csv")
df_test = pd.read_csv(r"C:\Users\ADMIN\Downloads\test.csv")

# Combine datasets for preprocessing
df = pd.concat([df_train, df_test], ignore_index=True)

# -------------------------------
# Basic Information
# -------------------------------
print(df.head())
print(df.info())

# -------------------------------
# Drop Unnecessary Columns
# -------------------------------
df.drop("User_ID", axis=1, inplace=True)

# -------------------------------
# Handle Gender Column
# -------------------------------
df["Gender"] = df["Gender"].map({"F": 0, "M": 1})

# -------------------------------
# Encode Age Column
# -------------------------------
label_encoder = preprocessing.LabelEncoder()
df["Age"] = label_encoder.fit_transform(df["Age"])

# -------------------------------
# One-Hot Encoding for City Category
# -------------------------------
df_city = pd.get_dummies(df["City_Category"])

df = pd.concat([df, df_city], axis=1)
df.drop("City_Category", axis=1, inplace=True)

# -------------------------------
# Handle Missing Values
# -------------------------------

# Product Category 2
mode_pc2 = df["Product_Category_2"].mode()[0]
df["Product_Category_2"] = df["Product_Category_2"].fillna(mode_pc2)

# Product Category 3
mode_pc3 = df["Product_Category_3"].mode()[0]
df["Product_Category_3"] = df["Product_Category_3"].fillna(mode_pc3)

# -------------------------------
# Handle Stay_In_Current_City_Years
# -------------------------------
df["Stay_In_Current_City_Years"] = (
    df["Stay_In_Current_City_Years"]
    .str.replace("+", "", regex=False)
    .astype(int)
)

# -------------------------------
# Exploratory Data Analysis
# -------------------------------

# Purchase vs Age
sns.barplot(x="Age", y="Purchase", hue="Gender", data=df)
plt.title("Purchase by Age and Gender")
plt.show()

# Purchase vs Occupation
sns.barplot(x="Occupation", y="Purchase", hue="Gender", data=df)
plt.title("Purchase by Occupation and Gender")
plt.show()

# -------------------------------
# Prepare Data for Machine Learning
# -------------------------------

# Separate processed train data
df_train_processed = df[df["Purchase"].notnull()]

X = df_train_processed.drop(["Purchase", "Product_ID"], axis=1)
y = df_train_processed["Purchase"]

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Feature Scaling
# -------------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)