"""Численное интегрирование"""
import math

import numpy
from matplotlib import pyplot


def function(x):
    # функция
    return math.sin(x)


def methodRectangle(n, a=0, b=10):
    # метод прямугольников
    result = 0
    h = (b - a) / n
    x = a
    for i in range(n):
        result += function(x + 0.5 * h)
        x += h
    return h * result


def methodTrapezoid(n, a=0, b=10):
    # метод трапеций
    result = 0
    h = (b - a) / n
    x = a + h
    for i in range(1, n):
        result += function(x)
        x += h
    return h * ((function(a) + function(b)) / 2 + result)

def methodKotes(n, a=0, b=10):
    # метод Котеса
    result = 0
    h = (b - a) / n
    x = a + h
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * function(x)
        else:
            result += 4 * function(x)
        x += h
    return (h / 3) * (function(a) + result + function(b))


def main():
    # начальные значения
    start = 0
    end = math.pi
    steps = 1000

    print(f'Метод прямоугольников : {methodRectangle(steps, start, end)}')
    print(f'Метод трапеций : {methodTrapezoid(steps, start, end)}')
    print(f'Метод Котеса : {methodKotes(steps, start, end)}')

    # правильные координаты
    x = numpy.linspace(0, 2 * end, steps)
    y = []
    for i in x:
        y.append(1 - math.cos(i))

    # погрешность различными методами
    y_rectangle = []
    y_trapezoid = []
    y_kotes = []
    for i in x:
        y_rectangle.append(methodRectangle(steps, 0, i) - (1 - math.cos(i)))
        y_trapezoid.append(methodTrapezoid(steps, 0, i) - (1 - math.cos(i)))
        y_kotes.append(methodKotes(steps, 0, i) - (1 - math.cos(i)))

    # построение графиков
    # pyplot.plot(x, y, label = "sin(x)")
    pyplot.plot(x, y_rectangle, label = "Погрешность методом прямоугольников" )
    pyplot.plot(x, y_trapezoid, label="Погрешность методом трапеций")
    pyplot.plot(x, y_kotes, label="Погрешность методом Котеса")
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    main()