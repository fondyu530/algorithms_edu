def find_sum_existence(s, x):
    s = sorted(s)
    for i in range(len(s)-1):
        left_index = i + 1
        right_index = len(s) - 1
        while left_index <= right_index:
            middle = (left_index + right_index) // 2
            elements_sum = s[i] + s[middle]
            if elements_sum == x:
                return True
            elif x < elements_sum:
                right_index = middle - 1
            else:
                left_index = middle + 1
    return False


input_s = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(-10, 25):
    print(i, find_sum_existence(input_s, i))
