"""
Разыгрывание случайной величины
Исследование Random-функции, создать большой массив псевдослучайных чисел, узнать сколько ра
повторяются первые 5 чисел в таком же порядке (псевдопериод), посчитать мат.ожидание, дисперсию.
Сформировать Случайную величину с наперед заданными значениями и их вероятностями (задание дискретной СВ)
"""

import random
import numpy
import time


def main():
    # Иницилизация случайных величин
    random.seed(time.time())
    n = 1000000
    randNumbers = [random.randint(0, 9) for i in range(n)]

    # Поиск повторов первых пяти чисел
    findNumbers = randNumbers[:5]
    k = 0
    for i in range(len(randNumbers) - 5):
        if randNumbers[i:i+5] == findNumbers:
            k += 1

    print(f'Количество повторений первых пяти чисел: {k}')

    # Вычисление математического ожидания и дисперсии с помощью библиотеки numpy
    mathMeanNumpy = numpy.mean(randNumbers)
    varianceNumpy = numpy.var(randNumbers)

    print(f'Математическое ожидание (numpy): {mathMeanNumpy}')
    print(f'Дисперсия (numpy): {varianceNumpy}')

    specialValues, counts = numpy.unique(randNumbers, return_counts=True)

    # Вычисление математического ожидания
    mathMean = 0
    for i in range(len(specialValues)):
        mathMean += specialValues[i] * counts[i] / n
    print(f'Математическое ожидание: {mathMean}')

    mathMeanMid = 0
    for i in range(len(randNumbers)):
        mathMeanMid += randNumbers[i]
    mathMeanMid /= n
    print(f'Математическое ожидание (среднее): {mathMeanMid}')

    # Вычисление дисперсии
    midSum = 0
    for i in randNumbers:
        midSum += i
    midSum /= n

    variance = 0
    for i in range(len(randNumbers)):
        variance += (randNumbers[i] - midSum) ** 2
    variance /= n
    print(f'Дисперсия: {variance}')

    # Создание дискретной случайной величины с заданными значениями и вероятностями
    numbers = [i for i in range(0, 10)]
    chance = [0.1 for i in range(0, 10)]

    # Генерация случайной величины с использованием заданных значений и вероятностей
    discreteNumbers = numpy.random.choice(numbers, p=chance)

    print(f'Случайная величина:{discreteNumbers}')

    # Вычисление вероятностей для каждого значения дискретной случайной величины
    samples = numpy.random.choice(numbers, size=n, p=chance)
    unique, counts = numpy.unique(samples, return_counts=True)

    print("Вероятности для каждого значения дискретной случайной величины:")
    for i in range(len(unique)):
        print(f'Значеник: {unique[i]}, Вероятность: {counts[i] / n}')


if __name__ == "__main__":
    main()