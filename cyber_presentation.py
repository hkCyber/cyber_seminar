# from urllib.request import urlretrieve
from sklearn.linear_model import LinearRegression
# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
# import japanize_matplotlib
# import seaborn as sns
# import io


# x = [[10], [20], [30]]
# y = [30,50,80]
#
# lr = LinearRegression()
# lr.fit(x, y)
#
# source = [[33]]
# predicted = lr.predict(source)
# print("Predicted Result: ")
# print('x(気温):', source)
# print('y(ビール消費支出):', predicted)
#
# plt.scatter(x, y, color = 'blue')         # 説明変数と目的変数のデータ点の散布図をプロット
# plt.plot(x, lr.predict(x), color = 'red') # 回帰直線をプロット
#
# plt.title('Regression Line')               # 図のタイトル
# plt.xlabel('気温') # x軸のラベル
# plt.ylabel('ビール消費支出')    # y軸のラベル
# plt.grid()                                 # グリッド線を表示
#
# plt.show()

#2
import numpy as np
x = np.array([10, 20, 30])
y = np.array([30, 50, 80])

n=len(x)
t_xy=sum(x*y)-(1/n)*sum(x)*sum(y)
t_xx=sum(x**2)-(1/n)*sum(x)**2
slope=t_xy/t_xx
intercept=(1/n)*sum(y)-(1/n)*slope*sum(x)
print('傾き=',slope,'切片=',intercept)
predict_x=intercept+slope*x
print('予測値=',predict_x)
resudial_y=y-predict_x
print('残差=',resudial_y)

