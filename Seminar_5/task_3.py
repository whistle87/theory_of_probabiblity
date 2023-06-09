"""
Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что уровень значимости 1%? (Провести двусторонний тест.)
"""
from scipy import stats
import numpy

x = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
alfa = 0.01
M_0 = 200
n = 10
# выбираем t критерий, так как не знаем среднеквадратичное отклонение генеральной совокупности
t_1 = stats.t.ppf(alfa / 2, df=(n - 1))  # -3.2498355440153697
t_2 = stats.t.ppf(1 - (alfa / 2), df=(n - 1))  # 3.2498355440153697
print(t_1, t_2)
# среднее по выборке
mean_x = numpy.mean(x)  # 198.5
std_x = numpy.std(x, ddof=1)
t_x = (mean_x - M_0) / (std_x / (n ** 0.5))  # -1.0651074037450896
# t_x  не попадает критическую область, значит мы не отвергаем нулевую гипотезу
# делаем вывод, что среднее заначение веса пачек из выборки статистически не отличается
# от среднего генеральной совокупности и равен в стреднем 200 гр.
