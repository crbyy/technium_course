class MyDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def __getitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            return self._values[index]
        else:
            return None

    def __setitem__(self, key, value):
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __delitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            self._values.pop(index)
            self._keys.pop(index)

    def __contains__(self, key):
        if key in self._keys:
            return True
        else:
            return False

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        listed = []
        for i in range(len(self._keys)):
            pair = self._keys[i], self._values[i]
            listed.append(pair)
        return listed


    def __str__(self):
        items = []
        for i in range(len(self._keys)):
            items.append(f"{self._keys[i]} : {self._values[i]}")
        return "{" + ", ".join(items) + "}"




my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
# print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict.items())
print(my_dict)

