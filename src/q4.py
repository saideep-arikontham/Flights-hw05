'''
print the carrier, tail number, month and day for each flight
order the results by these fields (in the order specified)
get only those flights for which the plane is a made by "AIRBUS INDUSTRIE"
get only the first 10 flights
'''
import pandas as pd #1.5.3
from readit import get_con, get_query_results

con = get_con()
df = get_query_results("SELECT * FROM planes", con)
print('USING JOINS:')
df1 = get_query_results('SELECT f.carrier, f.tailnum, f.month, f.day, f.flight FROM flights f inner join planes p on p.tailnum = f.tailnum where p.manufacturer = "AIRBUS INDUSTRIE" order by f.carrier, f.tailnum, f.month, f.day limit 10', con)
print(df1)

print('\n\nUSING WHERE:')
df2 = get_query_results('SELECT carrier, tailnum, month, day, flight FROM flights where tailnum in (select tailnum from planes where manufacturer = "AIRBUS INDUSTRIE") order by carrier, tailnum, month, day limit 10', con)
print(df2)