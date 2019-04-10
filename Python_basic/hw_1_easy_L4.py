# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


a = [1, 2, 4, 0]
b = [i**2 for i in a]
print(b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


fruits_1 = ['яблоко', 'апельсин', 'груша', 'банан']
fruits_2 = ['яблоко', 'мандарин', 'груша', 'ананас']
result_list = list(set([fruit for fruit in fruits_1 + fruits_2 if (fruits_1 + fruits_2).count(fruit) > 1]))
print(result_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


numbers = list(range(-10, 10))
print(numbers)
result_list = [i for i in numbers if i % 3 == 0 or i > 0 or i % 4 == 0]
print(result_list)
