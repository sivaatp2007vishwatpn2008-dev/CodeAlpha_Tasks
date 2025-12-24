#Importing Libraries
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np 

#Dataset for analysis
df=pd.read_csv(r"C:\Users\Easwar\Desktop\CodeAlpha_Project\books.csv")
print("Sample Data : \n",df.head(5))
print("Data Shape : \n",df.shape)
print("Data Coloumns : \n",df.columns)
print("Data Types : \n",df.dtypes)
print("Data Description : \n",df.describe)

data=df.copy()
print(df.isna().sum())
print("No Missing Values")

#Visualizing Data
#Histplot
plt.figure(figsize=(6,4))
sns.histplot(df['Price'], bins=30, kde=True)
plt.title('Distribution of Books Price')
plt.xlabel('Books')
plt.ylabel('Price')
plt.show()

#Box plot
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Price'])
plt.title('Box Plot of Books Price')
plt.show()

#Bar chart
plt.figure(figsize=(6,4))
sns.countplot(x='Stock', data=df)
plt.title('Frequency of Stock')
plt.xticks(rotation=45)
plt.show()

#Scatter plot
plt.figure(figsize=(6,4))
sns.scatterplot(x='Price', y='SI_NO', data=df)
plt.title('Relationship between Books & Price ')
plt.show()

#Heat map
plt.figure(figsize=(10,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()



