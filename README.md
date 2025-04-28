# Exploratory_Data_Analysis
Rows = 892
Columns = 12
Contains information about passengers such as age, gender, ticket fare, class, and survival status.
Initial data exploration using .info() revealed missing values in the 'Age' and 'Cabin' columns, with 'Cabin' missing the most data. 
The .describe() function showed that the average age of passengers was around 30 years and the average fare paid was approximately 32.20 units, with significant variation.
A bar plot of gender distribution confirmed that males were the majority on board. 
A scatterplot between 'Age' and 'Fare' indicated no strong visible relationship between the two variables. 
A boxplot comparing 'Age' across 'Sex' categories showed that females had a slightly lower median age compared to males. 
Correlation analysis using a heatmap revealed that 'Fare' was moderately correlated with 'Survived', and 'Pclass' was negatively correlated with both 'Fare' and 'Survived'. 
A pairplot further illustrated that first-class passengers had a higher survival rate and that younger passengers had a slightly better chance of survival. 
From this analysis, key insights include that women and higher-class passengers were more likely to survive, higher fare prices were associated with higher survival chances, and most passengers were young adults.
These trends align with historical knowledge about Titanic's survival patterns, where social status and gender heavily influenced survival rates.
