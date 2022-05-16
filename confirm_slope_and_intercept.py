import numpy as np
x = np.array([10, 20, 30])
y = np.array([30, 50, 80])

n = len(x)
t_xy = sum(x * y) - (1/n) * sum(x) * sum(y)
t_xx = sum(x ** 2) - (1/n) * sum(x) ** 2
slope=t_xy/t_xx
intercept = (1/n) * sum(y) - (1/n) * slope * sum(x)
print('傾き=', slope, '切片=', intercept)
predict_x = intercept + slope*x
print('予測値=', predict_x)
resudial_y = y - predict_x
print('残差=', resudial_y)

