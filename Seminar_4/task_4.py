"""
Рост взрослого населения города X имеет нормальное распределение, причем,
средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см.
посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.),
а затем проверить себя с помощью встроенных функций
"""
from scipy import stats

M = 174
sd = 8
# 1. больше 182 см?
z = (182 - M) / sd  # z = 1, по таблице находим долю для этого значения 0.8413
F_taller_182 = 1 - 0.8413  # 0.1587
F_taller_182_python = 1 - stats.norm.cdf(182, loc=M, scale=8)  # 0.15865525393145707
print(F_taller_182, F_taller_182_python)
# 2. больше 190 см?
z = (190 - M) / sd  # z = 2, по таблице находим долю для этого значения 0.9772
F_taller_190 = 1 - 0.9772  # 0.0228
F_taller_190_python = 1 - stats.norm.cdf(190, loc=M, scale=8)  # 0.02275013194817921
print(F_taller_190, F_taller_190_python)
# 3. от 166 см до 190 см?
z = (166 - M) / sd  # z = -1, по таблице находим долю для этого значения 0.1587
F_from_166_to_190 = 0.9772 - 0.1587  # 0.8185
F_from_166_to_190_python = stats.norm.cdf(190, loc=M, scale=8) - stats.norm.cdf(166, loc=M,
                                                                                scale=8)  # 0.8185946141203637
print(F_from_166_to_190, F_from_166_to_190_python)
# 4. от 166 см до 182 см?
F_from_166_to_182 = 0.8413 - 0.1587  # 0.6826
F_from_166_to_182_python = stats.norm.cdf(182, loc=M, scale=8) - stats.norm.cdf(166, loc=M,
                                                                                scale=8)  # 0.6826894921370859
print(F_from_166_to_182, F_from_166_to_182_python)
# 5. от 158 см до 190 см?
z = (158 - M) / sd  # z = -2, по таблице находим долю для этого значения 0.0228
F_from_158_to_190 = 0.9772 - 0.0228  # 0.9544
F_from_158_to_190_python = stats.norm.cdf(190, loc=M, scale=8) - stats.norm.cdf(158, loc=M,
                                                                                scale=8)  # 0.9544997361036416
print(F_from_158_to_190, F_from_158_to_190_python)
# 6. не выше 150 см или не ниже 190 см?
z = (150 - M) / sd  # z = -3, по таблице находим долю для этого значения 0.0013
F_to_150_and_taller_190 = 0.0013 + F_taller_190  # 0.0241
F_to_150_and_taller_190_python = stats.norm.cdf(150, loc=M, scale=8) + F_taller_190_python  # 0.0241000299798093
print(F_to_150_and_taller_190, F_to_150_and_taller_190_python)
# 7. не выше 150 см или не ниже 198 см?
z = (198 - M) / sd  # z = 3, по таблице находим долю для этого значения 0.9987
F_to_150_and_taller_198 = 0.0013 + (1 - 0.9987)  # 0.0026
F_to_150_and_taller_198_python = stats.norm.cdf(150, loc=M, scale=8) + (
            1 - stats.norm.cdf(198, loc=M, scale=8))  # 0.0026997960632601965
print(F_to_150_and_taller_198, F_to_150_and_taller_198_python)
# 8. ниже 166 см?
z = (166 - M) / sd  # z = -1, по таблице находим долю для этого значения 0.1587
F_to_166 = 0.1587
F_to_166_python = stats.norm.cdf(166, loc=M, scale=8)  # 0.15865525393145707
print(F_to_166, F_to_166_python)
