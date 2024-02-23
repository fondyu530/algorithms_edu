def binary_numbers_sum(fst_binary_array: list, scd_binary_array: list) -> list:
    fst_binary_array_size = len(fst_binary_array)
    scd_binary_array_size = len(scd_binary_array)
    if fst_binary_array_size == scd_binary_array_size:
        result_binary_array = []
        temp_digit = 0
        for i in range(fst_binary_array_size-1, -1, -1):
            fst_binary_array_digit = fst_binary_array[i]
            scd_binary_array_digit = scd_binary_array[i]
            digits_sum = fst_binary_array_digit + scd_binary_array_digit + temp_digit
            if digits_sum < 2:
                temp_digit = 0
            elif digits_sum == 2:
                temp_digit = 1
                digits_sum = 0
            elif digits_sum == 3:
                temp_digit = 1
                digits_sum = 1
            result_binary_array.insert(0, digits_sum)
        result_binary_array.insert(0, temp_digit)
        return result_binary_array


a = [1, 1, 1, 1, 1]
b = [1, 1, 1, 1, 1]
c = binary_numbers_sum(a, b)
print(c)
