import pandas as pd
import json
from sqlalchemy import create_engine

with open('jsondata.json', encoding='utf-8') as j:
    data = json.load(j)

df = pd.DataFrame(data)
df = df.applymap(lambda x: x if x != '' else None)
# engine = create_engine('postgresql://postgres:dheeraj1902@localhost:5432/visualization_dashboard')

# df.to_sql('data', engine, if_exists='append', index=False)
# df.to_csv('js_data1.csv', index=False)
print(df.describe())
