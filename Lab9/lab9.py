"""Красно-черное дерево"""

class Node:
    def __init__(self, data, color='red', left=None, right=None, parent=None):
        self.data = data
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class Tree:
    # Конструктор
    def __init__(self):
        # При инициализации создаётся пустой узел, им обозначаются листья
        self.TNULL = Node(0)
        self.TNULL.color = 'black'
        self.root = self.TNULL

    # Операция вставки
    def insert(self, item):
        insertNode = Node(item)
        insertNode.left = self.TNULL
        insertNode.right = self.TNULL

        previusNode = None
        currentNode = self.root

        self.print()
        # Добираемся до узла вставки
        while currentNode != self.TNULL:
            previusNode = currentNode
            if insertNode.data < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        # Определяем кореневой узел
        insertNode.parent = previusNode

        # Условие для первой вставки (корневой узел)
        if previusNode is None:
            self.root = insertNode

        # Определяем вставка это левый или правый дочерний узел
        elif insertNode.data < previusNode.data:
            previusNode.left = insertNode
        else:
            previusNode.right = insertNode

        # Меняем цвет корневому узлу при первой вствке
        if insertNode.parent is None:
            insertNode.color = 'black'
            return

        # Условие на отсутствие необходимости в балансирвоке
        if insertNode.parent.parent is None:
            return

        # Балансировка дерева
        self.insertFix(insertNode)

    # Левый поворот
    def leftRotate(self, node):
        # Установка как правого ребёнка
        swapNode = node.right
        # Перемещение левого ребёнка
        node.right = swapNode.left
        # Обновление родительской ссылки у левого ребёнка
        if swapNode.left != self.TNULL:
            swapNode.left.parent = node
        # Обновление родительской ссылки
        swapNode.parent = node.parent
        # Условие на установку коря
        if node.parent is None:
            self.root = swapNode
        # Если node был левым ребёнком, то swapNode становится левым
        elif node == node.parent.left:
            node.parent.left = swapNode
        # Если node был правым ребёнком, то swapNode становится правым
        else:
            node.parent.right = swapNode
        # node становится левым ребёнком swapNode
        swapNode.left = node
        # swapNode становится родителем node
        node.parent = swapNode

    # Правый поворот
    def rightRotate(self, node):
        # Установка как левого ребёнка
        swapNode = node.left
        # Перемещение правого ребёнка
        node.left = swapNode.right
        # Обновление родительской ссылки у левого ребёнка
        if swapNode.right != self.TNULL:
            swapNode.right.parent = node
        # Обновление родительской ссылки
        swapNode.parent = node.parent
        # Условие на установку корня
        if node.parent is None: # Если node был корнем
            self.root = self
        # Если node был правым ребёнком, то swapNode становится правым
        elif node == node.parent.right:
            node.parent.right = swapNode
        # Если node был левым ребёнком, то swapNode становится левым
        else:
            node.parent.left = swapNode
        # node становится правым ребёнком swapNode
        swapNode.right = node
        # swapNode становится родителем node
        node.parent = swapNode

    # Операция балансировки
    def insertFix(self, insertNode):
        # Пока родитель нового узла красный
        while insertNode.parent.color == 'red':
            # Если родитель является правым ребёнком
            if insertNode.parent == insertNode.parent.parent.right:
                uncleNode = insertNode.parent.parent.left
                # Если дядя красный
                if uncleNode.color == 'red':
                    uncleNode.color = 'black'
                    insertNode.parent.color = 'black'
                    insertNode.parent.parent.color = 'red'
                    # Фиксация на уровне деда
                    insertNode = insertNode.parent.parent
                # Если дядя черный
                else:
                    # Если ребёнок является левым
                    if insertNode == insertNode.parent.left:
                        insertNode = insertNode.parent
                        # Правое вращение вокруг родителя
                        self.rightRotate(insertNode)
                    insertNode.parent.color = 'black'
                    insertNode.parent.parent.color = 'red'
                    # Левое вращение вокруг деда
                    self.leftRotate(insertNode.parent.parent)
            # Если родитель является левым ребёнком
            else:
                uncleNode = insertNode.parent.parent.right
                # Если дядя красный
                if uncleNode.color == 'red':
                    uncleNode = 'black'
                    insertNode.parent.color = 'black'
                    insertNode.parent.parent.color = 'red'
                    # Фиксация на уровне деда
                    insertNode = insertNode.parent.parent
                else:
                    # Если ребёнок является правым
                    if insertNode == insertNode.parent.right:
                        insertNode = insertNode.parent
                        # Левое вращение вокруг родителя
                        self.leftRotate(insertNode)
                    insertNode.parent.color = 'black'
                    insertNode.parent.parent.color = 'red'
                    # Правое вращение вокруг деда
                    self.rightRotate(insertNode.parent.parent)
            # Условие для первой вставки
            if insertNode == self.root:
                break
        # Корень всегда должен быть черным
        self.root.color = 'black'

    def printHelper(self, node):
        if node != self.TNULL:
            self.printHelper(node.left)
            print(node.data, end=' ')
            self.printHelper(node.right)

    def print(self):
        self.printHelper(self.root)
        print()

def main():
    tree = Tree()
    numbers = [8, 7, 11, 2, 3, 4, 5, 1, 6, 9, 10]
    for num in numbers:
        tree.insert(num)
    tree.print()

if __name__ == '__main__':
    main()