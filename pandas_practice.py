import pandas as pd

songs = {'Artist': ['Michael Jackson', 'AC/DC', 'Pink Floyd', 'Whitney Houston', 'Meat Loaf', 'Eagles', 'Bee Gees', 'Fleetwood Mac'], 'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'], 'Released': [1982, 1980, 1973, 1992, 1977, 1976, 1977, 1977], 'Length': ['0:42:19', '0:42:11', '0:42:49', '0:57:44', '0:46:33', '0:43:08', '1:15:54', '0:40:01'], 'Genre': ['pop, rock, R&B', 'hard rock', 'progressive rock', 'R&B, soul, pop', 'hard rock, progressive rock', 'rock, soft rock, folk rock', 'disco', 'soft rock'], 'Music Recording Sales (millions)': [46.0, 26.1, 24.2, 27.4, 20.6, 32.2, 20.6, 27.9], 'Claimed Sales (millions)': [65, 50, 45, 44, 43, 42, 40, 40], 'Released.1': ['30-Nov-82', '25-Jul-80', '01-Mar-73', '17-Nov-92', '21-Oct-77', '17-Feb-76', '15-Nov-77', '04-Feb-77'], 'Soundtrack': ['nan', 'nan', 'nan', 'Y', 'nan', 'nan', 'Y', 'nan'], 'Rating': [10.0, 9.5, 9.0, 8.5, 8.0, 7.5, 7.0, 6.5]}

# df = pd.DataFrame(songs)
# print(df)
# print(df['Length']) # getting length of songs
# print(df['Artist'].unique())  # Getting unique value from name column
# df1 = df[df['Released'] > 2000] # getting song above released year 2000
# print(df1)
# df.to_csv('song.csv')

"""
DataFrame Attributes and Methods
DataFrames provide numerous attributes and methods for data manipulation and analysis, including:

shape: Returns the dimensions (number of rows and columns) of the DataFrame.
info(): Provides a summary of the DataFrame, including data types and non-null counts.
describe(): Generates summary statistics for numerical columns.
head(), tail(): Displays the first or last n rows of the DataFrame.
mean(), sum(), min(), max(): Calculate summary statistics for columns.
sort_values(): Sort the DataFrame by one or more columns.
groupby(): Group data based on specific columns for aggregation.
fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
apply(): Apply a function to each element, row, or column of the DataFrame.
"""

# df = pd.read_csv('song.csv')
# print(df.loc[2, 'Released']) # .loc[] take first input num and second column name
# print(df.iloc[2, 5]) # .iloc[] only take integer as row number or column number
# print(df[['Artist', 'Album']])

# xl = pd.read_excel(r"C:\Users\DELL\Downloads\input_txt.xlsx")

# text = xl['text'].tolist()
# print(text)
# print(len(text))

csv_file = [f'csvs/Output{f}.csv' for f in range(0, 11)]

concatenated_df = pd.DataFrame()

excel_writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
excel_writer.book.create_sheet('Sheet1', 0)
sheet = excel_writer.sheets['Sheet1']

row_offset = 0

# Iterate through each CSV file
for idx, file_path in enumerate(csv_file, 1):
    # Read the CSV into a DataFrame
    df = pd.read_csv(file_path)
    
    # Concatenate the DataFrame vertically
    concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)
    

    # Write the DataFrame to the Excel sheet
    df.to_excel(excel_writer, sheet_name='Sheet1', startrow=row_offset, index=False, header=True)

    # Add two blank rows after each table
    row_offset += df.shape[0] + 2

# Save the Excel file
excel_writer._save()