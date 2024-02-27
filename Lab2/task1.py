def function(x):
    return x**2 - 2

def methodBisection(a, b, DELTA):
    # предусловие
    if function(a) * function(b) > 0:
        print("Условие не выполнено, повторите ввод")
        return
    # делаем пока интервал не будет меньше погрешности
    while (b - a) / 2 > DELTA:
        c = (a + b) / 2
        # нашли ответ
        if function(c) == 0:
            return c
        # определяем половину
        elif function(a) * function(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

def main():
    print(methodBisection(0, 3, 0.00001))

if __name__ == "__main__":
    main()