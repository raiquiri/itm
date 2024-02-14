x = [[1, -1], [2, 1]]
b = [-5, -7]


def methodGausse():
    for i in range(0, len(x) - 1):
        factor = x[i+1][0] / x[i][0]
        for j in range(len(x[i])):
            x[i+1][j] -= x[i][j] * factor
        b[i+1] -= b[i] * factor
        
def variableFind():
    k = 1
    variable = b[len(b)] / x[len(x)-1][len(x[len(x)-1])]
    arr = [variable]
    print('Переменная №1 = ', variable)
    for i in range(len(x) - 2, -1):
        numSum = 0
        for j in range(len(x[i]) - 1, len(x[i]) - 1 - k):
            numSum += x[i][j] * arr[len(arr) - j]
        variable = b[i]



def main():
    pass


if __name__ == "__main__":
    main()
