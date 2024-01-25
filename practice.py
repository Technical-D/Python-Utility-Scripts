import pandas as pd
import matplotlib.pyplot as plt
# print(pd.__version__)

" 1. Write a Pandas program to read a csv file from a specified source and print the first 5 rows"
diamonds = pd.read_csv('diamonds.csv')
# print(diamonds.head())

"2. Write a Pandas program to read a dataset from diamonds DataFrame and modify the default columns values and print the first 6 rows."

columns = ['carat', 'cut', 'x', 'y', 'z']
# print(diamonds[columns].head(6))

"3. Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series. (hint: print any of the columns from data frame)"

# print(diamonds['carat'])

"4. Write a Pandas program to create a new 'Quality -color' Series (use bracket notation to define the Series name) of the diamonds DataFrame"

# diamonds['Quality-color'] = diamonds['cut'] +', '+diamonds['color']

# print(diamonds.head())

"5. Write a Pandas program to find the number of rows and columns and data type of each column of diamonds Dataframe."

# print(diamonds.shape) # Give number of row and columns
# print(diamonds.dtypes) # Data type of ech column
# print(diamonds.info()) # Give both of above info

"6. Write a Pandas program to summarize only 'object' columns of the diamonds Dataframe."
# Give the summary for data like count, mean, std etc...
# print(diamonds.describe(include='object')) # For object type only 
# print(diamonds.describe()) # For numeric only
# print(diamonds.describe(include='all')) # For very data type

"7. Write a Pandas program to rename two of the columns of the diamonds Dataframe."
# Inplace=True will change original data frame 
# Inplace=False will not change original data frmae instead you can save the change o=in new data frame
# diamonds.rename(columns={'CUT': 'cut', 'CARAT': 'carat'},inplace=True)
# print(diamonds.head())

"8. Write a Pandas program to rename all the columns of the diamonds Dataframe."

diamonds.drop('Unnamed: 0', axis=1, inplace=True)

new_col_name = ['new_carat', 'new_cut', 'new_color', 'new_clarity', 'new_depth', 'new_table', 'new_price', 'new_x', 'new_y', 'new_z', 'new_quality-color']
# diamonds.columns = new_col_name
# print(diamonds.head())

"9. Write a Pandas program to remove the second column of the diamonds Dataframe."

# diamonds.drop('cut', axis=1, inplace=True)
# print(diamonds.head())

"10. Write a Pandas program to remove multiple columns at once of the diamonds Dataframe."

# diamonds.drop(['cut', 'carat', 'x'], axis=1, inplace=True)
# print(diamonds.head())

"11. Write a Pandas program to remove multiple rows at once (axis=0 refers to rows) from diamonds dataframe."

# diamonds.drop([1,5, 7], axis=0, inplace=True)
# print(diamonds.head())

"12. Write a Pandas program to sort the 'cut' Series in ascending order (returns a Series) of diamonds Dataframe."

# df = diamonds.sort_values('cut') # Sorted all the data frame by col=vut
# "or"
# res = diamonds['cut'].sort_values(ascending=True) # Sorted only col=cut

# print(res.head())

"13. Write a Pandas program to sort the 'price' Series in descending order (returns a Series) of diamonds Dataframe"

# sor = diamonds['price'].sort_values(ascending=False)
# print(sor)

"14. Write a Pandas program to sort the entire diamonds DataFrame by the 'carat' Series in ascending and descending order."

# sorted_df_as = diamonds.sort_values(by='carat', ascending=True)
# sorted_df_dsc = diamonds.sort_values(by='carat', ascending=False)
# print(sorted_df_as)
# print(sorted_df_dsc)

"15. Write a Pandas program to filter the DataFrame rows to only show carat weight at least 0.3."

# res = diamonds[diamonds['carat'] >= 0.3]
# print(res)

"16. Write a Pandas program to convert a python list to pandas series."

# carat = diamonds['carat'].to_list()
# series = pd.Series(carat)
# print(series)

"7. Write a Pandas program to find the details of the diamonds where length>5, width>5 and depth>5."

# res = diamonds[(diamonds['x'] > 5) & (diamonds['y'] > 5) & (diamonds['z'] >5)]
# print(res)

"18. Write a Pandas program to find the diamonds that are either Premium or Ideal."

# res = diamonds[(diamonds['cut'] == 'Premium') | (diamonds['cut'] =='Ideal')]
# "or"
# res = diamonds[diamonds['cut'].isin(['Premium', 'Ideal'])]
# print(res)

"19. Write a Pandas program to find the diamonds that are with a Fair or Good or Premium."

# res = diamonds[diamonds['cut'].isin(['Fair', 'Good', 'Premium'])]
# print(res)

"20. Write a Pandas program to display all column labels of diamonds DataFrame."

# col_labels = diamonds.columns
# print(col_labels)

"21. Write a Pandas program to read only a subset of 3 rows from diamonds DataFrame."

# rows = diamonds.iloc[:10, :6]
# rows = diamonds.iloc[:3]
# print(rows)

"22. Write a Pandas program to iterate through diamonds DataFrame."

# for d in diamonds:
#     print(d)

# This will properlt iterate through data frame
# for index, row in diamonds.iterrows():
#     print(index, row)
#     if index == 10:
#         break

"23. Write a Pandas program to drop all non-numeric columns from diamonds DataFrame."


# for c in diamonds.columns:
#     if diamonds[c].dtype == 'object':
#         diamonds.drop(c, axis=1, inplace=True)
# "or"
# obj_col = diamonds.select_dtypes(include='object')
# diamonds.drop(obj_col, axis=1,inplace=True)
# print(diamonds.head())

"24. Write a Pandas program to include only numeric columns in the diamonds DataFrame."
import numpy as np
# print(diamonds.select_dtypes(include=np.number))
# "or"
# print(diamonds.select_dtypes(include='number'))


"25. Write a Pandas program to pass a list of data types to only describe certain types of diamonds DataFrame."

# print(diamonds.select_dtypes(include=[np.int64, np.float64,'object']))
# "or"
# print(diamonds.select_dtypes(include=['int64', 'float64','object']))

"26. Write a Pandas program to calculate the mean of each numeric column of diamonds DataFrame."

# df = diamonds.select_dtypes(include=np.number)
# print(df.mean())

# mean = diamonds['carat'].mean()
# print(mean)

"27. Write a Pandas program to calculate the mean of each row of diamonds DataFrame."

# df = diamonds.select_dtypes(include=np.number)
# mean = df.mean(axis=1)
# print(mean.head())  

"28. Write a Pandas program to calculate the mean of price for each cut of diamonds DataFrame."

# res = diamonds.groupby('cut')['price'].mean()
# print(res)

"29. Write a Pandas program to calculate count, minimum, maximum price for each cut of diamonds DataFrame."

# res = diamonds.groupby('cut')['price'].agg(['sum', 'min', 'max', 'count'])
# print(res)

"30. Write a Pandas program to create a side-by-side bar plot of the diamonds DataFrame."

# cut_counts = diamonds['cut'].value_counts()
# cut_counts.plot(kind='bar', color=['blue', 'green', 'red', 'purple', 'orange'])
# plt.xlabel('Cut')
# plt.ylabel('Count')
# plt.title('Diamond Cut Counts')
# plt.savefig('plot.png')

"31. Write a Pandas program to count how many times each value in cut series of diamonds DataFrame occurs."

# res = diamonds['cut'].value_counts()
# print(res)

"32. Write a Pandas program to display percentages of each value of cut series occurs in diamonds DataFrame."

# res = diamonds['cut'].value_counts(normalize=True) * 100
# print(type(res))

"33. Write a Pandas program to display the unique values in cut series of diamonds DataFrame."

# res = diamonds['cut'].unique() # Gives unique value from column
# print(res)

"34. Write a Pandas program to count the number of unique values in cut series of diamonds DataFrame."

# res = diamonds['cut'].nunique() # Give number of unique values in column
# print(res)

"35. Write a Pandas program to compute a cross-tabulation of two Series in diamonds DataFrame."

# res = pd.crosstab(diamonds['cut'], diamonds['color'])
# print(res)

"36. Write a Pandas program to calculate various summary statistics of cut series of diamonds DataFrame."

res = diamonds['cut'].describe()
print(res)