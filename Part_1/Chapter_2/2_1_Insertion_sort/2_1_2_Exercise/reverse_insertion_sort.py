def reverse_insertion_sort(lst: list):
    list_size = len(lst)
    for i in range(list_size-2, 0, -1):
        j = i + 1
        edge_val = lst[i]
        while j < list_size and edge_val < lst[j]:
            lst[j-1] = lst[j]
            j += 1
        lst[j-1] = edge_val


input_list = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
reverse_insertion_sort(input_list)
print(input_list)
