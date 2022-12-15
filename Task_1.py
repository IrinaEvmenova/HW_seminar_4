# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

# 10^(-1)≤d≤10^(-10)

from math import pi

def format_by_mask(num: float, accuracy: float) -> float:
    '''Форматирует число по заданной маске'''
    accuracy = str(accuracy)
    accuracy = len(accuracy[accuracy.find('.')+1::])
    return float(f'{pi:0.{accuracy}f}')

d = input('Введите точность к числу Пи:\n')
print(format_by_mask(pi, d))