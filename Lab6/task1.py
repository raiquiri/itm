"""Интерполяция (многочлен Лагранжа) Бояршинов М.Г. - Численные методы ч.4"""
import numpy
from matplotlib import pyplot

def methodLagrange(xValues, yValues, x):

    """
    :param xValues: исходые данные значения х
    :param yValues: исходные данные значения у
    :param x: точка, для которой необходимо найти соответствующий у

    :return: у соответсвуюищй заданому х
    """
    result = 0
    for i in range(len(xValues)):
        step = yValues[i]
        for j in range(len(xValues)):
            if j != i:
                # Вычисляем многочлен Лагранжа для каждой точки
                step *= (x - xValues[j]) / (xValues[i] - xValues[j])
        result += step
    return result

def main():
    x = 3
    # количество узлов для исходных данных
    stepCount = 5

    xValues = numpy.linspace(-2, 2, stepCount + 1)
    yValues = numpy.abs(xValues)

    xIValues = numpy.linspace(-2, 2, 100)
    yIValues = methodLagrange(xValues, yValues, xIValues)

    pyplot.plot(xIValues, numpy.abs(xIValues), label='Функция y = |x|')
    pyplot.plot(xIValues, yIValues, label='Интерполяция Лагранжа')
    pyplot.scatter(xValues, yValues, color='red', label='Исходные данные')
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.legend()
    pyplot.grid(True)
    pyplot.show()


    print(f'x = {xValues}')
    print(f'y = {yValues}')

    print(f'при x = {x} -> y = {numpy.round(methodLagrange(xValues, yValues, x), 2)}')

if __name__ == "__main__":
    main()


