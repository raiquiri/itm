def gauss(A, B):
    n = len(A)

    # прямой ход метода Гаусса
    for i in range(n):
        max_index = i
        # цикл для избегания ошибок / перестановка строк местами
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
        B[i], B[max_index] = B[max_index], B[i]

        # прямой ход начинается
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                # пересчёт основной матрицы
                A[j][k] -= factor * A[i][k]
            # пересчёт матрицы вектора
            B[j] -= factor * B[i]

    # обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        # счёт переменной
        x[i] = B[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            # вычитание известного
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