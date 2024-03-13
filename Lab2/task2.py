"""Метод простых итераций, a - начальное значение, maxIteration - кол-во итераций, DELTA - погрешность"""

def function(x):
    # функция для схождения
    return (x + 2/x) / 2


def methodSimpleI(a, maxIteration, DELTA):
    # начальное значение
    x0 = a
    for i in range(maxIteration):
        # уточненное значение
        x1 = function(x0)
        # проверка на погрешность / ответ
        if abs(x1 - x0) < DELTA:
            return x1
        x0 = x1
    # выход из функции, если не получилось найти ответ
    return None


def main():
    print(methodSimpleI(0.1, 1000, 0.001))


if __name__ == "__main__":
    main()