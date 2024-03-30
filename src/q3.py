import pandas as pd #1.5.3
from readit import get_con, get_query_results

con = get_con()
df = get_query_results("SELECT * FROM flights", con)

print('Number of rows where primary key is id in flights table: ',df.shape[0])
df1 = df[['year', 'month', 'day', 'hour','flight','arr_delay']]
df2 = df1.groupby(['year', 'month', 'day', 'hour','flight']).mean().reset_index()
print('Number of unique rows values for the given columns from the original data : ',df2.shape[0])

if(df.shape[0] == df2.shape[0]):
    print("The columns 'year', 'month', 'day', 'hour','flight' can be used as primary key")
else:
    print('Total duplicated rows: ', df1[df1.duplicated(['year', 'month', 'day', 'hour','flight'], keep=False)].shape[0])
    print('Number of rows of unique duplicate rows : ',df1[df1.duplicated(['year', 'month', 'day', 'hour','flight'], keep='first')].shape[0])
    print("\n\nThe columns 'year', 'month', 'day', 'hour','flight' CANNOT BE USED as primary key as there are duplicate rows for these columns")
