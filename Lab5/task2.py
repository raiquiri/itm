"""Решение дифференциальных уравнений (Метод Рунге-Кутты 2-го порядка)"""
import numpy
from matplotlib import pyplot

"""
    x`` + x = t; x(0) = 0
"""

def function(x, v, t):
    """
        Выше написанное уравнение разложили на систему уравнений
        x` = v
        v` = t - x
    """
    dx_dt = v
    dv_dt = t - x
    return dx_dt, dv_dt


def methodRunge(function, initialConditions, stepSize, stepCount):
    """
        Входные данные:
        function - функция, описывающая уравнние
        initialConditions - начальные данные
        stepSize - величина шага
        stepCount - кол-во шагов

        Выходные данные:
        xValues - значение х на каждом шаге
        vValues - значение производной х на каждом шаге
    """
    xValues = numpy.zeros(stepCount + 1)
    vValues = numpy.zeros(stepCount + 1)

    xValues[0], vValues[0] = initialConditions

    for i in range(stepCount):
        x = xValues[i]
        v = vValues[i]
        t = i * stepSize

        k1x, k1v = function(x, v, t)
        k2x, k2v = function(x + stepSize * k1x, v + stepSize * k1v, t + stepSize)

        xValues[i + 1] = x + 0.5 * stepSize * (k1x + k2x)
        vValues[i + 1] = v + 0.5 * stepSize * (k1v + k2v)

    return xValues, vValues


def analiticSolution(t):
    return t - numpy.sin(t)


def main():
    initialConditions = [0, 0]
    stepSize = 0.1
    stepCount = 100

    xValues, vValues = methodRunge(function, initialConditions, stepSize, stepCount)
    tValues = numpy.linspace(0, stepSize * stepCount, stepCount + 1)
    analiticValues = analiticSolution(tValues)
    errorValues = numpy.abs(xValues - analiticValues)

    # pyplot.plot(tValues, analiticValues, label="Истинный график")
    pyplot.plot(tValues, xValues, label="x(t)")
    pyplot.plot(tValues, vValues, label="v(t)")
    # pyplot.plot(tValues, errorValues, label="Погрешность")
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    main()
