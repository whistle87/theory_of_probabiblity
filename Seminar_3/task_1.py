"""
Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий
для данной выборки.
"""

salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
mean = 0
for el in salary:
    mean = mean + el
mean = mean / len(salary)
sum_of_squares = 0
for el in salary:
    sum_of_squares = (el - mean) ** 2 + sum_of_squares
non_shifted_dispersion = sum_of_squares / (len(salary) - 1)
shifted_dispersion = sum_of_squares / len(salary)
var = shifted_dispersion ** (0.5)
print(f"Среднее значение: {mean}\nСреднее квадратичное отклонение: {var}\nСмещенная дисперсия: {shifted_dispersion}"
      f"\nНесмещенная дисперсия :{non_shifted_dispersion}")
