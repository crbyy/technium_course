
def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)


print("Отсортированный список:", my_list)