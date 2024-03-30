import pandas as pd #1.5.3
import seaborn as sns
import matplotlib.pyplot as plt
from readit import get_con, get_query_results

con = get_con()
df = get_query_results("SELECT * FROM flights", con)
print(df.shape)
sns.scatterplot(data = df, y = df['arr_delay'], x = df['distance'], color = 'orange')

dfk = df[df['distance'] > 3000]
print(f'It is clear that when distance is greater than 3000 units, we get outliers. The unique values for destination when distance is greater than 3000 units are: {dfk.dest.unique()}. Therefore remove rows with those destinations to remove outliers.')
#verify: df[(df['dest'] == 'HNL') | (df['dest'] == 'ANC')].shape is equal to dfk.shape()

df1 = df[(df['dest'] != 'HNL') & (df['dest'] != 'ANC')]
print(df1.shape)
sns.scatterplot(data = df1, y = df1['arr_delay'], x = df1['distance'])

plt.savefig('figs/scatter_dist_vs_delay.png')
plt.show()

sns.set_theme(style="ticks")

g = sns.jointplot(data=df1, y="arr_delay", x="distance", marginal_ticks=True)

plt.savefig('figs/jointplot_dist_vs_delay.png')
plt.show()