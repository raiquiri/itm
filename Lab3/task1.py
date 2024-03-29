"""Численное дифференцирование"""
import math
import matplotlib.pyplot as plt

def numDerSim(function, x, h = 1e-8):
    # функция для вычисления значения производной  конечные разности (симметричная)
    return (function(x + h) - function(x -h)) / (2 * h)



def numDerLeft(function, x, h = 1e-5):
    # функция для вычисления значения производной  конечные разности (левая)
    return (function(x) - function(x - h)) / h


def numDerRight(function, x, h = 1e-5):
    # функция для вычисления значения производной  конечные разности (правая)
    return (function(x + h) - function(x)) / h

def derFunction(x):
    # производная от функции
    return math.cos(x)

def myFunction(x):
    # функция
    return math.sin(x)


def main():
    # инициализация массивов
    x = []
    y = []
    # производная в точке на инетравале [0, 4pi]
    for i in range(0, 10 * int(4*math.pi) + 1, 1):
        x.append(i / 10)
        y.append(derFunction(i / 10) - numDerSim(myFunction, i / 10))

    # построение графика
    plt.plot(x, y, label = "Кривая 1")
    plt.xlabel('x')  # подпись оси x
    plt.ylabel('y')  # подпись оси y
    plt.title('График двух кривых')  # заголовок графика
    plt.legend()  # вывод легенды
    plt.show()  # вывод графика


if __name__ == "__main__":
    main()