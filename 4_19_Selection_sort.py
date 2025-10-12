
def selection_sort(arr):
    n = len(arr)

    for i in range(0, n):
        min_index = i
        for next_index in range(min_index + 1, n):
            if arr[next_index] < arr[min_index]:
                min_index = next_index

        arr[i], arr[min_index] = arr[min_index], arr[i]


my_list = [64, 34, 25, 12, 22, 11, 90]

selection_sort(my_list)
print("Отсортированный список:", my_list)