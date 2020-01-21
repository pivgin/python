# Практическое задание
# 1: Даны два произвольные списка.
# Удалите из первого списка элементы присутствующие во втором списке.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет:
# [5, 8]

print('Task_1. Lists')
print('------------||------------')
print()
my_list_1 = [13, 5, 13, 8, 2, 13, 13, 4, 6]
my_list_2 = [2, 7, 13, 3]
my_list_3 = []
my_list_4 = []
i = int(input('Input the number of elements in massive 1: '))
j = int(input('Input the number of elements in massive 2: '))
# values for 1st list
while i > 0:
    item = int(input('Number: '))
    my_list_3.append(item)
    i -=1
print(my_list_3)
# values for 2nd list
while j > 0:
    item = int(input('Number: '))
    my_list_4.append(item)
    j -= 1
print(my_list_4)
print()
# actual work cycle
# for val in my_list_1:
#     if val in my_list_2:
#         my_list_1.remove(val)
# print(my_list_1)
# фор не правільно работает так как значенія удаляются
int = len(my_list_4)
while int != 0:
    for val in my_list_4:
        if val in my_list_3:
            my_list_3.remove(val)
    int -= 1
print(my_list_3)