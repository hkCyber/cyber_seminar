from urllib.request import urlretrieve
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns

# download
urlretrieve("https://raw.githubusercontent.com/kujirahand/book-mlearn-gyomu/master/src/ch2/tenki/kion10y.csv", "kion10y.csv")

# read 10 years data of temperature
df1 = pd.read_csv("kion10y.csv", encoding="utf-8")
df2 = pd.read_csv("/Users/bami/Downloads/kakei/all.csv")

df = pd.merge(df1, df2, on=['年', '月', '日'])
df['気温'] = np.round(df['気温'], decimals = 0)

df.drop(df[df['月'] > 11].index, inplace = True)

g = df.groupby(["気温"])["ビール消費支出"]
gg = g.sum() / g.count()

print(gg)
gg.plot()
plt.savefig("consumed_beer_per_temp.png")
plt.show()

df.plot.scatter(x='気温', y='ビール消費支出', alpha=0.1)
plt.show()
