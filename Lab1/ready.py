def gauss(A, B):
    n = len(A)

    # прямой ход метода Гаусса
    for i in range(n):
        # Выбор главного элемента
        max_index = i
        for j in range(i + 1, n):
            B[i], B[max_index] = B[max_index], B[i]

            # Приведение к верхнетреугольному виду
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    # обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            B[j] -= A[j][i] * x[i]

    return x




def main():
    A = [[3, 2, -5],
         [2, -1, 3],
         [1, 2, -1]]

    B = [-1, 13, 9]

    print("Решение:", gauss(A, B))

if __name__ == "__main__":
    main()