"""Метод Ньютона, х0 - начальное значение, DELTA - погрешность"""

def function(x):
    return x**2 - 2

def functionP(x):
    # производная
    return x*2

def methodNewton(x0, DELTA):
    while True:
        # точки пересечения касательной
        x1 = x0 - function(x0) / functionP(x0)
        # проверка на погрешность / выход из цикла
        if abs(x1 - x0) < DELTA:
            break
        x0 = x1
    return x1

def main():
    print(methodNewton(0.1, 0.0001))

if __name__ == "__main__":
    main()