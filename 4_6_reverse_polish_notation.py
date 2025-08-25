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

expression = "3425*+-"

for token in expression:
    if token in "+-*/":
        if token == "+":
            stack1.push(stack1.pop() + stack1.pop())
        if token == "-":
            stack1.push(stack1.pop() - stack1.pop())
        if token == "*":
            stack1.push(stack1.pop() * stack1.pop())
        if token == "/":
            stack1.push(stack1.pop() / stack1.pop())
            print(f'#4 {stack1.display_stack()}')
    else:
        stack1.push(int(token))

print(stack1.display_stack())
