class Stack:
    def __init__(self):
        self.items = [] # список для хранения элементов

    def display_stack(self):
        return f'ITEMS: {self.items}'

    def is_empty(self):
        return len(self.items) == 0 # пустой ли стек (список элементов)

    def push(self, item):
        self.items.append(item) # добавляет элемент в стек (в конец списка)

    def pop(self):
        if not self.is_empty():
            return self.items.pop() # удаляет + возвращает элемент из стека (последний добавленный)
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1] # Возвращает не удаляет последни элемент стека
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items) # возвращает длину стека




stack1 = Stack()

skobka_pustaya = ''
skobka_pravilnaya = '([]{})'
skobka_pravilnaya2 = '()'
skobka_nepravilnaya = '(((]{'

skobka_slovar = {')': '(', ']': '[', '}': '{'}

for skobka in skobka_nepravilnaya:
    if skobka in '([{':
        stack1.push(skobka)
    if skobka in ')]}':
        last_skobka = stack1.peek()
        if last_skobka == skobka_slovar[skobka]:
            stack1.pop() #



if stack1.is_empty():
    print("Скобочная последовательность верна.")
else:
    print("Скобочная последовательность неверна.")




