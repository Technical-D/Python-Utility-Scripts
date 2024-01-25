import psycopg2

conn = psycopg2.connect(
    database= "visualization_dashboard",
    user = 'postgres',
    password = 'dheeraj1902',
    host = 'localhost',
    port = '5432'
)

# Create a cursor object
# cur = conn.cursor()

# company_data = [(5, 'Acme Corporation', '5555555555', '123 Oak St, City, State', 'Technology', 2010, True, 'USA'),
#     (6, 'Beta Industries', '7777777777', '456 Elm Rd, Town, Province', 'Manufacturing', 2007, True, 'Canada'),
#     (7, 'Gamma Ltd.', '9999999999', '789 Maple Dr, Village, Region', 'Finance', 2013, True, 'UK'),
#     (8, 'Delta Enterprises', '2222222222', '456 Birch Ln, City, State', 'Healthcare', 2009, True, 'Australia'),
#     (9, 'Epsilon Solutions', '3333333333', '789 Pine Ave, Town, Province', 'Technology', 2016, True, 'USA'),
#     (10, 'Zeta Innovations', '5555555555', '123 Cedar Rd, City, State', 'Finance', 2005, True, 'Canada'),
#     (11, 'Eta Systems', '7777777777', '456 Redwood Dr, Village, Region', 'Manufacturing', 2011, True, 'UK'),
#     (12, 'Theta Group', '9999999999', '789 Sequoia Ln, Town, Province', 'Healthcare', 2004, True, 'Australia')]

# for data in company_data:
#     query = f"INSERT INTO company VALUES({data[0]}, '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', {data[5]}, {data[6]}, '{data[7]}');"
#     cur.execute(query)

# cur.close()
# conn.commit()
# conn.close()

# Using pandas
import pandas as pd

df = pd.read_sql_query('Select * from data', conn)
# print(df.columns)
# print(df.describe(include='all'))
# df.to_csv('js_data.csv',index=False)

print(df.describe())