import sqlite3
import pandas as pd #1.5.3

def get_con():
    return sqlite3.connect('data/mydb.sqlite')

def get_query_results(query,con):
    return pd.read_sql_query(query, con)