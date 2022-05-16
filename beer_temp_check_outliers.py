from urllib.request import urlretrieve
import pandas as pd
import beer_temp_config as conf

# download　気象データ
urlretrieve("https://raw.githubusercontent.com/kujirahand/book-mlearn-gyomu/master/src/ch2/tenki/kion10y.csv", "kion10y.csv")

# read 11 years data of temperature
df1 = pd.read_csv("kion10y.csv", encoding="utf-8")
df2 = pd.read_csv(conf.csv_filepath_for_beer_expenses, encoding="utf-8")
df = pd.merge(df1, df2, on=['年', '月', '日'])

outliers = df.query('ビール消費支出 > 100')
print(outliers)
