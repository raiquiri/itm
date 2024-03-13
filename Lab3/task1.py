"""Численная дифференциация"""

def numDer(function, x, h = 1e-5):
    # функция для вычисления значения производной / конечные разности
    return (function(x + h) - function(x -h)) / (2 * h)

def myFunction(x):
    # функция
    return x**2 + 2*x + 1

def main():
    x = 3 # точка в которой считается производная
    result = numDer(myFunction, x)
    print(f'Значение производной в точке {x} = {result}')

if __name__ == "__main__":
    main()