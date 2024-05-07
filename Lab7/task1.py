"""Сортировки (пузырьковая, рукурсивная, суммированием)"""

# Пузырьковая сортировка
def bubbleSort(array):
    # Цикл для прохода по всем элементом массива
    for i in range(len(array)):
        # Второй цикл для сравения
        for j in range(i+1, len(array)):
            if (array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array

# Рекурсивная сортировка
def quickSort(array):

    # Условие выхода
    if len(array) <= 1:
        return array

    # Основной элемент от которого отталкивается алгоритм
    element = array[0]
    # Элементы меньше основного
    left = list(filter(lambda x: x < element, array))
    # Элементы равные основному
    center = [i for i in array if i == element]
    # Элементы больше основного
    right = list(filter(lambda x: x > element, array))

    # Элементы левее и правее будут раскалдывать на списки до тех пор,
    # пока не установится правильный порядок
    return quickSort(left) + center + quickSort(right)


def countSort(array):
    # Массив подсчета
    counts = [0] * (max(array) - min(array) + 1)

    # Подсчёт встречающихся элементов
    for num in array:
        counts[num - min(array)] += 1

    # Восстанавливаем отсортированный массив с помощью досчитанных значений
    subArray = []
    for i, count in enumerate(counts):
        subArray.extend([i + min(array)] * count)

    return subArray

def main():
    array = [13, 1, 2, 4, 23, 6]

    arrayBubble = bubbleSort(array[:])
    arrayQuick = quickSort(array[:])
    arrayCount = countSort(array[:])

    print(f'Initial Conditions:\n{array}\nBubble Sort:\n{arrayBubble}\n'
          f'Quick Sort:\n{arrayQuick}\nCounting Sort:\n{arrayCount}')



if __name__ == "__main__":
    main()