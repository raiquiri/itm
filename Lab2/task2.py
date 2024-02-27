def function(x):
    return (x + 2) ** 0.5


def methodSimpleI(a, maxIteration, DELTA):
    x0 = a
    for i in range(maxIteration):
        x1 = function(x0)
        if abs(x1 - x0) < DELTA:
            return x1
        x0 = x1
    return None


def main():
    print(methodSimpleI(0, 1000, 0.001))


if __name__ == "__main__":
    main()
