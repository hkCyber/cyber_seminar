#出典：政府統計の総合窓口(e-Stat)（https://www.e-stat.go.jp/）
#「家計調査の品目分類によるい別支出の二人以上の世帯・勤労者世帯」を加工して作成

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
# df.drop(df[df['月'] > 11].index, inplace = True)

df['日付'] = pd.to_datetime({'year': df['年'], 'month': df['月'], 'day': df['日']})
df['日付'] = df.index

plt.plot(df['日付'], df['ビール消費支出'])
plt.show()


