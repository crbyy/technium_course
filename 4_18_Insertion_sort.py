
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current  = arr[i]
        previous  = i - 1
        while previous >= 0 and arr[previous] > current:
            arr[previous + 1] = arr[previous]
            previous -= 1
        arr[previous + 1] = current


my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)


print("Отсортированный список:", my_list)