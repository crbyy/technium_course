class Queue:
    def __init__(self):
        self.items = [] # список для хранения элементов

    def display_queue(self):
        return f'ITEMS: {self.items}'

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0  # пустая ли очередь (список элементов)

    def size(self):
        return len(self.items)


queue1 = Queue()

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)

print("Размер очереди:", queue1.size())  # Размер очереди: 3

while not queue1.is_empty():
    item = queue1.dequeue()
    print("Извлечен элемент:", item)


