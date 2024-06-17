my_list = my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

list_len = len(my_list)
number_repeat = list_len - 1

i = 0
value = my_list[i]

while value >= 0:
    print(value)
    if i < number_repeat:
        i = i + 1
        value = my_list[i]
    else:
        break
