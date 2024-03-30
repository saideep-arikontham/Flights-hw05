import pandas as pd #1.5.3
import seaborn as sns
import matplotlib.pyplot as plt
from readit import get_con, get_query_results

con = get_con()
df = get_query_results("SELECT * FROM flights", con)

df1 = df[['dest','arr_delay','distance']].groupby('dest').mean()
sns.scatterplot(data = df1, x = df1['arr_delay'], y = df1['distance'])
plt.savefig('figs/grouped_scatter_delay_vs_distance.png')
plt.show()