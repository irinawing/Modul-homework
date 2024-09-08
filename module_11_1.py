import matplotlib.pyplot as plt
import pandas as pnd
import numpy as np


# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.

x = np.linspace(0, 2, 100)  # использование массива numpy
print(x)

# Задание: данные с помощью библиотеки любым удобным для вас инструментом из библиотеки
# далее используем созданный массив для значений

plt.figure(figsize=(5, 2.7), layout='constrained')

plt.plot(x, x, label='линейная зависимость')
plt.plot(x, x**2, label='парабола')
plt.plot(x, x**3, label='кубическая')
plt.grid(True)

plt.xlabel('x ось')
plt.ylabel('y ось')
plt.title("Простое уравнение")
plt.legend()
plt.show()

# Задание: считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль

Data = [1, 3, 4, 5, 6, 2, 9]
s = pnd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
si = pnd.Series(Data, Index)
print(si, " код pandas")

s = pnd.Series(["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"])

print(s.str.upper())

