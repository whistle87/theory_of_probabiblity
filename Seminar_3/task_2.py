"""
 В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
 Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча.
 Какова вероятность того, что 3 мяча белые?
"""
import math


def Bernoulli(n, k, p):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * \
           (p ** k) * ((1 - p) ** (n - k))


P_3 = Bernoulli(2, 0, 5 / 8) * Bernoulli(4, 3, 5 / 12) + \
      Bernoulli(2, 1, 5 / 8) * Bernoulli(4, 2, 5 / 12) + \
      Bernoulli(2, 1, 5 / 8) * Bernoulli(4, 1, 5 / 12)

print(P_3)
