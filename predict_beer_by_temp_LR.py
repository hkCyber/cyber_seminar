from urllib.request import urlretrieve
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import beer_temp_config as conf

# download
urlretrieve("https://raw.githubusercontent.com/kujirahand/book-mlearn-gyomu/master/src/ch2/tenki/kion10y.csv", "kion10y.csv")

# 11年間分のデータをデータフレームに格納し年月日でマージ
df1 = pd.read_csv("kion10y.csv", encoding="utf-8")
df2 = pd.read_csv(conf.csv_filepath_for_beer_expenses, encoding="utf-8")

df = pd.merge(df1, df2, on=['年', '月', '日'])

# 必要なデータのみを説明変数xに気温、目的変数yにビール消費支出を格納
x = []
y = list(df['ビール消費支出'])

temps = list(df['気温'])
for i in range(len(temps)):
    xa = []
    xa.append(temps[i])
    x.append(xa)

print(x)
print(y)


# 線形回帰で学習しモデル作成
model = LinearRegression()
model.fit(x, y)

# 予測のためのサンプルとその表示
for i in range(1, 34):
    source = [[33]]
    predicted = model.predict(source)
    print("予測した値: ")
    print('x(気温):', source)
    print('y(ビール消費支出):', predicted)

# 散布図のプロットと表示
plt.scatter(x, y, color = 'blue') # 説明変数と目的変数のデータ点の散布図をプロット
plt.plot(x, model.predict(x), color = 'red') # 回帰直線をプロット

plt.title('回帰直線') # 図のタイトル
plt.xlabel('気温') # x軸のラベル
plt.ylabel('ビール消費支出') # y軸のラベル
plt.grid() # グリッド線を表示
plt.show()
