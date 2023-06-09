"""
Задача 1. Известно, что генеральная совокупность распределена нормально
со средним квадратическим отклонением, равным 16.
Найти доверительный интервал для оценки математического ожидания с надежностью 0.95,
если выборочная средняя M = 80, а объем выборки n = 256.
"""
from scipy import stats

alfa = 0.05
z = round(stats.norm.ppf(alfa / 2), 2)  # z = -1.96
M = 80
n = 256
SD = 16

right_border = M - z * (SD / (n ** 0.5))  # 81.96
left_border = M + z * (SD / (n ** 0.5))  # 78.04
# C вероятностью 95% математическое ожидание генеральной совокупности будет в интервале [78.04;81.96]
