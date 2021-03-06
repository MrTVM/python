# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 1
for fruit in fruits:
    print("{}. {:>{}}".format(i, fruit, 6))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

random_list_1 = [1, 2, 3, 6]
random_list_2 = [4, 5, 6, 3]
print(set(random_list_1) - set(random_list_2))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [2, 3, 6, 10, 7, 5]
i = 0
for number in numbers:
    if (number % 2) == 0:
        numbers[i] = number / 4
    else:
        numbers[i] = number * 2
    i += 1
print(numbers)

