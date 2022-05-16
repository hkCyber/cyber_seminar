from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns

import beer_temp_config.py as conf

# download　気象データ
urlretrieve("https://raw.githubusercontent.com/kujirahand/book-mlearn-gyomu/master/src/ch2/tenki/kion10y.csv", "kion10y.csv")

# read 10 years data of temperature
df1 = pd.read_csv("kion10y.csv", encoding="utf-8")
df2 = pd.read_csv(conf.csv_filepath_for_beer_expenses, encoding="utf-8")

df = pd.merge(df1, df2, on=['年', '月', '日'])
df = df[(df['月'] < 12) & (df['日'] < 24)]
df = df[((df['月'] > 8) | (df['月'] < 8)) & (df['日'] > 14) | (df['日'] < 12)]

print(df.corr())
print(sns.heatmap(df.corr()))
plt.show()
