import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
df['Age'].hist(bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
sns.boxplot(x=df['Fare'])
plt.title('Fare Boxplot')
plt.show()
df['Sex'].value_counts().plot(kind='bar')
plt.title('Gender Distribution')
plt.show()
sns.scatterplot(x='Age', y='Fare', data=df)
plt.title('Age vs Fare')
plt.show()
sns.boxplot(x='Sex', y='Age', data=df)
plt.title('Age by Gender')
plt.show()
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
sns.pairplot(df, hue='Survived')
plt.show()
