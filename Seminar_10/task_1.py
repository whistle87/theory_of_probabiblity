"""
Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди
взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех группах случайно
выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
"""
import numpy as np
from scipy import stats
from scipy.stats import shapiro

football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

k = 3
n = len(football) + len(hockey) + len(weightlifters)
print(shapiro(football))  # statistic=0.9775082468986511, pvalue=0.9495404362678528
print(shapiro(hockey))  # statistic=0.9579196572303772, pvalue=0.7763139009475708
print(shapiro(weightlifters))  # statistic=0.9386808276176453, pvalue=0.5051165223121643
# Все выборки распределны нормально
print(stats.bartlett(football, hockey, weightlifters))  # statistic=0.4640521043406442, pvalue=0.7929254656083131
# делаем вывод, что дисперсии равны
# Значит для проведения дисперсионного анализа выбираем критерий Фишера

x_mean = np.mean(football)  # 179.125
y_mean = np.mean(hockey)  # 178.66666666666666
z_mean = np.mean(weightlifters)  # 172.72727272727272
total = np.array([173, 175, 180, 178, 177, 185, 183, 182, 177, 179, 180, 188, 177, 172,
                  171, 184, 180, 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
total_mean = np.mean(total)  # 176.46428571428572
# Сумма квадратов отклонений наблюдений от общего среднего
SST = np.sum((total - total_mean) ** 2)
# Сумма квадратов отклонений средних групповых значений от общего среднего
SSB = np.sum((x_mean - total_mean) ** 2) * len(football) + \
      np.sum((y_mean - total_mean) ** 2) * len(hockey) + \
      np.sum((z_mean - total_mean) ** 2) * len(weightlifters)
# остаточная сумма кваратов отклонений
SSW = np.sum((football - x_mean) ** 2) + np.sum((hockey - y_mean) ** 2) + np.sum((weightlifters - z_mean) ** 2)
D_f = SSB / (k - 1)
D_ost = SSW / (n - k)
F_n = D_f / D_ost  # 5.500053450812598

print(stats.f_oneway(football, hockey, weightlifters))  # statistic=5.500053450812596, pvalue=0.010482206918698693
# pvalue < 0.05 значит нулевую гипотезу не отвергаем,
# делаем вывод, что статитсически значимых разлиичй между группами не обнаруженно, 
# значит вид занятий не влияет на рост спортсмена
