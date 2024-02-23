def insertion_sort(lst: list):
    list_size = len(lst)
    for i in range(1, list_size):
        j = i - 1
        edge_val = lst[i]
        while j >= 0 and edge_val < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = edge_val


input_list = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
insertion_sort(input_list)
print(input_list)
