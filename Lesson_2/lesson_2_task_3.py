import math

def square(side):
    return math.ceil(side ** 2)

side = float(input('Введите сторону квадрата: '))
area = square(side)
print('Площадь квадрата равна', area)
