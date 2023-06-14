"""
Задача 2. В результате 10 независимых измерений некоторой величины X, выполненных с
одинаковой точностью,
получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения
вероятностей, оценить истинное значение величины X при помощи доверительного интервала,
покрывающего это значение с доверительной вероятностью 0,95.
"""
import numpy
from scipy import stats

x = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
alfa = 0.05
n = 10
# Истинное значение величины равно ее математическому ожиданию
mean_x = numpy.mean(x)
t = round(stats.t.ppf(alfa / 2, n - 1), 2)  # -2.26
sigma_x = numpy.std(x, ddof=1)  # 0.4508017549014448
left_border = mean_x + t * sigma_x / numpy.sqrt(n)  # 6.267823367976165
right_border = mean_x - t * sigma_x / numpy.sqrt(n)  # 6.9121766320238365
# с вероятностью 95% истинное значение величины х находится в интревале [6.27; 6.91]