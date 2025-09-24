class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

    def __repr__(self):
        return f'Node({self.value})' ####

class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        stack = Stack()
        visited_node = []

        stack.push(self._root)

        while not stack.is_empty():
            node = stack.pop()
            if node not in visited_node:
                visited_node.append(node)

                for neighbor in reversed(node.outbound):
                    stack.push(neighbor)

                # for neighbor in (node.outbound):
                #     stack.push(neighbor)

        return visited_node


class Stack:
    def __init__(self):
        self.items = []

    def display_stack(self):
        return f'ITEMS: {self.items}'

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)



# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# a.point_to(b)
# b.point_to(c)
# c.point_to(d)
# d.point_to(a)
# b.point_to(d)


# a = Node('a')
# b = Node('b')
# c = Node('c')
# a.point_to(b)
# b.point_to(c)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
c.point_to(e)


g = Graph(a)

print(g.dfs())