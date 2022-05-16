from urllib.request import urlretrieve
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import beer_temp_config as conf

# download　気象データ
urlretrieve("https://raw.githubusercontent.com/kujirahand/book-mlearn-gyomu/master/src/ch2/tenki/kion10y.csv", "kion10y.csv")

# 11年分の気象データとビール消費支出を取得し格納し年月日でマージ
df1 = pd.read_csv("kion10y.csv", encoding="utf-8")
df2 = pd.read_csv(conf.csv_filepath_for_beer_expenses, encoding="utf-8")
df = pd.merge(df1, df2, on=['年', '月', '日'])

# データを学習用とテストように分割する
train_year = (df["年"] <= 2015)
test_year = (df["年"] >= 2016)
interval = 6

# 過去6日分を学習するデータを作成
def make_data(data):
  x = [] # learning data
  y = [] # results
  temps = list(data["気温"])
  beers = list(data["ビール消費支出"])
  for i in range(len(temps)):
    if i < interval: continue
    y.append(beers[i])
    xa = []
    for p in range(interval):
      d = i + p - interval
      xa.append(temps[d])
    x.append(xa)
  return (x, y)

train_x, train_y = make_data(df[train_year])
test_x, test_y = make_data(df[test_year])

# 線形回帰分析を行う
lr = LinearRegression(normalize=True)
lr.fit(train_x, train_y) # learning
pre_y = lr.predict(test_x) # prediction

# 結果を図にプロット
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(test_y, c='r')
plt.plot(pre_y, c='b')
plt.savefig('tenki-kion-beer-lr.png')
plt.show()

# 評価
diff_y = abs(pre_y - test_y)
print("average=", sum(diff_y)/len(diff_y))
print("max=", max(diff_y))
