"""
Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные
автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из
n=100 шариков средний диаметр
оказался равным 17.5 мм, а дисперсия генеральной совокупности известна и равна 4 кв. мм
"""
from scipy import stats

# Н0 - среднее по выборке не отличается от среднего по генеральной совокупности.
# H1 - среднее по генеральной совкупности меньше среднего по выборке.
mean_general = 17
alfa = 0.05
n = 100
mean_x = 17.5
D = 4
z_x = (mean_x - mean_general) / ((D ** 0.5) / (n ** 0.5))  # z_x = 2.5
t_critical = stats.norm.ppf(1 - alfa)  # t_critical = 1.65
# z_x > t_critical, значит отвергаем нулевую гипотезу
# Делаем вывод, что средний диаметр шариков в генеральной совокупности больше 17 мм
