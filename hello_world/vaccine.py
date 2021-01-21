# Гениальный ученый по имени Рик изобрел вакцину против опасного вируса.
# Следующей целью Рика является изготовление и доставка наибольшего числа образцов вакцины в параллельные вселенные.
# К сожалению, его портальная технология не позволяет перемещаться в любые две соседние параллельные вселенные.
# Невозможно посетить как соседние вселенные текущей, в которой находится Рик, так и соседние вселенные уже посещенных ранее.
# Каждая вселенная по разным причинам имеет ограничение по количеству образцов вакцины, которые она может принять.
# Помогите Рику понять, сколько образцов вакцин ему надо изготовить, при условии,
# что его помощник Морти предоставит ему карту(список) вселенных и количество образцов вакцин,
# которые сможет принять каждая. Рику не известны эти данные заранее, придется разработать универсальный алгоритм.
#
# Входные данные - карта вселенных с ограничениями по количеству образцов вакцин (целочисленный массив неотрицательных чисел).
# Выходные данные - количество образцов вакцин, которое надо изготовить (целое неотрицательное число).
# Первая и последние вселенные не являются соседними в списке вселенных предоставленных Морти, при условии что в списке больше двух вселенных.
#
# Требования:
# Решением должна быть консольная программа на языке Python, принимающая на вход в качестве параметра программы целочисленный массив данных и возвращающая в консоль ответ как одно число.

print('Rick\'s vaccine')
print('------------||------------')
print()
# list_of_planets_ = [input('Input list of planets space separated')]
# print(list_of_planets_)

# number_of_planets = int(input('Input number of planets '))
# # if number_of_planets.isdigit() (
# list_of_planets_ = []
# i = 0
# while i < number_of_planets:
#     list_of_planets_.append(int(input('Input capacity of planet ')))
#     i += 1
# print(list_of_planets_)

# list_of_planets_ = [5, 2, 4, 3, 5, 6, 2]
list_of_planets_ = [5, 2, 4, 3, 5, 6, 2]
max_value = max(list_of_planets_)
print(max_value)
max_list_positions = [i for i, j in enumerate(list_of_planets_) if j == max_value]
print(max_list_positions)
copy_list_planets = list_of_planets_.copy()
print(copy_list_planets)
# slit by 3 elements
split_list = []
for i in range (0, len(copy_list_planets),3):
    split_list.append(copy_list_planets[i : i+3])
print(split_list)
print(split_list[0])
print(len(split_list))
best_list = []
increment = 0
# for i in range (0,len(split_list[0])):
for j in range(0, len(split_list)-1):
    if split_list[j][0] + split_list[j][2] > split_list[j][1]:
        best_list.append(0+increment)
        best_list.append(2+increment)
    else:
        best_list.append(1)
    print(best_list)
    increment += 3

print(increment)
print ('-----------last part---------')
last_mass_number = len(split_list)-1
print (last_mass_number)
print(increment)
last_list = []
last_list = split_list[last_mass_number].copy()
if len(last_list) == 1:
    best_list.append(0+increment)
elif len(last_list) == 2:
    max_last_list_positions = [n for n, m in enumerate(last_list) if m == max(last_list)]
    for i in range (0,len(max_last_list_positions)):
        max_last_list_positions[i] += increment
        best_list.append(max_last_list_positions[i])
else:
    if (split_list[last_mass_number][0] + split_list[last_mass_number][2]) > (split_list[last_mass_number][1]):
        best_list.append(0+increment)
        best_list.append(2+increment)
    else:
        best_list.append(1+increment)
print(best_list)
problem_elements = []

for i in range (1,len(best_list)-1):
    if ((best_list[i] - best_list[i+1]) == -1) or ((best_list[i-1] - best_list[i]) == -1):
        problem_elements.append(best_list[i])

if best_list[len(best_list)-1] - best_list[len(best_list)-2] == 1:
    problem_elements.append(best_list[len(best_list) - 1])

print(problem_elements)
print(copy_list_planets)
# priority of thirds
priority_list = []
temp_sum = 0
for i in range(0, len(split_list)-1):
    temp_sum = int(split_list[i][0] + split_list[i][2])
    if temp_sum > split_list[i][1]:
        priority_list.append(temp_sum)
    else:
        priority_list.append(split_list[i][1])

if len(last_list) == 1:
    priority_list.append(last_list[0])
elif len(last_list) == 2:
    priority_list.append(max(last_list))
else:
    if (last_list[0] + last_list[2]) > (last_list[1]):
        priority_list.append(last_list[0] + last_list[2])
    else:
        priority_list.append(last_list[1])
print(priority_list)
third_priority = priority_list.index(max(priority_list))
print(third_priority)
high_priority_list = split_list[third_priority]
print(high_priority_list)
third_increment = 0
if third_priority == 0:
    third_increment = 0
else:
    third_increment = third_priority + 2
# for i in range (0, 2):
#     if (i + third_increment) in best_list:
#         print('ok')
#     else:
#         best_list.remove(int(i + third_increment))
# print(best_list)
