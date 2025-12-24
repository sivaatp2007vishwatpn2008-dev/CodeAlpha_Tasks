#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Taking Spotify Dataset
df = pd.read_csv(r"C:\Users\Easwar\Desktop\CodeAlpha_Project\CodeAlpha_DataAnalysis\spotify_data clean.csv")
print("Sample Data : \n",df.head(5))

# Convert date column
df['album_release_date'] = pd.to_datetime(df['album_release_date'], errors='coerce')
print("Date Coloumns : \n" ,df['album_release_date'])

#Data Visualization Techniques
#Histograms
plt.figure(figsize=(6,4))
plt.hist(df['track_popularity'].dropna(), bins=30)
plt.title("Histogram of Track Popularity")
plt.xlabel("Popularity")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df['track_duration_min'].dropna(), bins=30)
plt.title("Histogram of Track Duration (Minutes)")
plt.xlabel("Duration")
plt.ylabel("Frequency")
plt.show()

#Box plots
plt.figure(figsize=(6,4))
sns.boxplot(x=df['artist_followers'])
plt.title("Box Plot of Artist Followers")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['track_popularity'])
plt.title("Box Plot of Track Popularity")
plt.show()

#Bar charts and Count plots
plt.figure(figsize=(6,4))
sns.countplot(x='album_type', data=df)
plt.title("Album Type Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='explicit', data=df)
plt.title("Explicit Content Distribution")
plt.show()

df['artist_name'].value_counts().head(10).plot(kind='bar', figsize=(7,4))
plt.title("Top 10 Artists by Track Count")
plt.ylabel("Number of Tracks")
plt.show()

#Scatter Plots
plt.figure(figsize=(6,4))
sns.scatterplot(
    x='artist_popularity',
    y='track_popularity',
    data=df,
    alpha=0.6
)
plt.title("Artist Popularity vs Track Popularity")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(
    x='track_duration_min',
    y='track_popularity',
    hue='album_type',
    data=df
)
plt.title("Duration vs Popularity by Album Type")
plt.show()

#Violin plots
plt.figure(figsize=(7,4))
sns.violinplot(x='album_type', y='track_popularity', data=df)
plt.title("Track Popularity Distribution by Album Type")
plt.show()

#Correlation Heatmap
corr = df.corr(numeric_only=True)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

#Pair plot
num_cols = df.select_dtypes(include=np.number).columns
sns.pairplot(df[num_cols].dropna().sample(500, random_state=42))
plt.show()

#Line plot
yearly = df['album_release_date'].dt.year.value_counts().sort_index()

plt.figure(figsize=(8,4))
plt.plot(yearly.index, yearly.values, marker='o')
plt.title("Tracks Released Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Tracks")
plt.show()

#Bar chart-aggregate
df.groupby('album_type')['track_popularity'].mean().plot(
    kind='bar', figsize=(6,4)
)
plt.title("Average Track Popularity by Album Type")
plt.ylabel("Average Popularity")
plt.show()

#Heatmap-pivot
pivot = pd.pivot_table(
    df,
    values='track_popularity',
    index='album_type',
    columns='explicit',
    aggfunc='mean'
)

plt.figure(figsize=(6,4))
sns.heatmap(pivot, annot=True, cmap='viridis')
plt.title("Avg Popularity by Album Type & Explicit Content")
plt.show()



