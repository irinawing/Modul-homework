number = int(input("Введите число от 3 до 20: "))

if number < 3 or number > 20:
    print("Введено неверное число!")
else:
    key = ""
    list = []

    for i in range (1, number-1):
        for j in range (i,number):
            if i != j:
                if number % (i + j) == 0 and number not in list:
                    key = key + str(i) + str(j)
                    list.append(str(i) + str(j))

    print("Ключ: ",key)

