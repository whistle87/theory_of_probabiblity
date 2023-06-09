"""
Исследовалось влияние препарата на уровень давления пациентов. Сначала
измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть
ли статистически значимые различия между измерениями давления? В выборках не соблюдается условие нормальности.
1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150, 130, 135
3е измерение через 30 минут: 130, 130, 120, 130, 125
"""
from scipy import stats

before = [150, 160, 165, 145, 155]
after_10_min = [140, 155, 150, 130, 135]
after_30_min = [130, 130, 120, 130, 125]
# Так как это повторные измерения и выборк больше 2-х, то при меняем критерий Фридмана
stats.friedmanchisquare(before, after_10_min, after_30_min)
# statistic=9.578947368421062, pvalue=0.00831683351100441
# pvalue < 0.05, значит отвергаем нулевую гипотезу
# Получается, что существуют статитсически заничмые различия на уровне заничимости 0.05
# Значит препарат работает
