import matplotlib.pyplot as plt
import pandas as pd
import beer_temp_config as conf

df = pd.read_csv(conf.csv_filepath_for_beer_expenses, encoding="utf-8")

g = df.groupby(['年', '月'])["ビール消費支出"]
gg = g.sum()/g.count()

print(gg)
gg.plot()
plt.xlabel('Month') # x軸のラベル
plt.ylabel('Beer Expense')    # y軸のラベル
plt.savefig("beer-heikin-tuki.png")
plt.show()
