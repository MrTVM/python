# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


names = ['Vladimir', 'Ivan', 'Alex', 'Anna']
salaries = [100, 120, 90, 500001]
print(dict(zip(names, salaries)))


def file_data(file_name, data):
    file_write = open(file_name, 'a+', encoding='utf-8')
    for name, salary in zip(data.keys(), data.values()):
        if salary < 500000:
            file_write.write("{} - {}\n".format(name, salary))
    file_write.close()


def file_read_data(file_name):
    file_read = open(file_name)
    for line in file_read:
        name_worker = line.strip().split(' - ')[0]
        salary_free_tax = float(line.strip().split(' - ')[1]) - (float(line.strip().split(' - ')[1]) * 0.13)
        print('{} - {} (после удержания налога)'.format(name_worker, round(salary_free_tax)))

    file_read.close()


file = 'salary.txt'
file_data(file, dict(zip(names, salaries)))
file_read_data(file)

