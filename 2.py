from statistics import mean
from numpy import var, std
from scipy import stats
from math import sqrt

ROUND_NUMBER = 3

# В результате 10 независимых измерений некоторой величины X,
# выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это значение с доверительной вероятностью 0,95.

x = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
t = stats.t.ppf(0.975, len(x)-1)
x_avg = mean(x)
x_std_n = std(x, ddof=1)
point_1 = x_avg-t*(x_std_n/sqrt(len(x)))
point_2 = x_avg+t*(x_std_n/sqrt(len(x)))
print(f'Доверительный интервал:[{round(point_1, ROUND_NUMBER)}; {round(point_2, ROUND_NUMBER)}]')
