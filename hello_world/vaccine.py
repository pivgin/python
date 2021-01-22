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

# Asking for list of planets section
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

# Program itself
list_of_planets_ = [5, 2, 4, 3, 5, 6, 2]
# list_of_planets_ = [4, 8, 5, 2]
# list_of_planets_ = [4, 2, 3, 4]
# list_of_planets_ = [5, 2, 4, 3, 5, 6, 2, 2]
# checking for max values
max_value = max(list_of_planets_)
# print('Max value is', max_value)
# checking for positions of max values
max_list_positions = [i for i, j in enumerate(list_of_planets_) if j == max_value]
# print('Positions of max elements', max_list_positions)
# creating copy of list of planets
copy_list_planets = list_of_planets_.copy()
print(copy_list_planets)
# slit whole list by 3 elements
split_list = []
for i in range(0, len(copy_list_planets), 3):
    split_list.append(copy_list_planets[i: i+3])
print('Slit list by 3 elements (split_list): ', split_list)
# print(split_list[0])
# print('Number of slit sections', len(split_list))
# Building up list with positions of all best values better to visit
best_list = []
increment = 0
# for i in range (0,len(split_list[0])):
for j in range(0, len(split_list)-1):
    if split_list[j][0] + split_list[j][2] > split_list[j][1]:
        best_list.append(0+increment)
        best_list.append(2+increment)
    else:
        best_list.append(1)
    # print(best_list)
    increment += 3

# print('-----------last part---------')
# Checking last section of initial list of planets
last_mass_number = len(split_list)-1
# print(last_mass_number)
# print(increment)
last_list = []
# creating copy of last section of planets
last_list = split_list[last_mass_number].copy()
if len(last_list) == 1:
    best_list.append(0+increment)
elif len(last_list) == 2:
    max_last_list_positions = [n for n, m in enumerate(last_list) if m == max(last_list)]
    for i in range(0, len(max_last_list_positions)):
        max_last_list_positions[i] += increment
        best_list.append(max_last_list_positions[i])
else:
    if (split_list[last_mass_number][0] + split_list[last_mass_number][2]) > (split_list[last_mass_number][1]):
        best_list.append(0+increment)
        best_list.append(2+increment)
    else:
        best_list.append(1+increment)
print('Positions of potentially best planets to visit (best_list): ', best_list)
# searching for problem elements on the boarders of split sections
problem_elements = []

for i in range(1, len(best_list)-1):
    if ((best_list[i] - best_list[i+1]) == -1) or ((best_list[i-1] - best_list[i]) == -1):
        problem_elements.append(best_list[i])

if best_list[len(best_list)-1] - best_list[len(best_list)-2] == 1:
    problem_elements.append(best_list[len(best_list) - 1])

print('List of positions of problem elements (problem_elements): ', problem_elements)
# print('Initial list of planets', copy_list_planets)
# priority of sections of thirds
priority_list = []
temp_sum = 0
for i in range(0, len(split_list)-1):                   # TODO looks like problem. Needed to be rewritten to check only problem sections
    temp_sum = int(split_list[i][0] + split_list[i][2])
    if temp_sum > split_list[i][1]:
        priority_list.append(temp_sum)
    else:
        priority_list.append(split_list[i][1])
# checking last priority of last section
if len(last_list) == 1:
    priority_list.append(last_list[0])
elif len(last_list) == 2:
    priority_list.append(max(last_list))
else:
    if (last_list[0] + last_list[2]) > (last_list[1]):
        priority_list.append(last_list[0] + last_list[2])
    else:
        priority_list.append(last_list[1])
print('List of max possible sums in sections of planets (priority_list): ', priority_list)
third_priority = priority_list.index(max(priority_list))
# print(third_priority)
high_priority_list = split_list[third_priority]
print('high_priority_list: ', high_priority_list)
# TODO add if verification for case with one max trio           almost done
max_priority_list = []
max_priority_list = [n for n, m in enumerate(priority_list) if m == max(priority_list)]
print('Positions of best trios (max_priority_list):', max_priority_list)
if len(max_priority_list) > 1:
    for i in range(0, len(max_priority_list)-1):
        if (split_list[i][1] + split_list[i+1][0]) < (split_list[i][2] + split_list[i+1][1]):       #TODO to make universal
            best_list.remove(split_list[i+1][0])     #TODO to make universal
        else:
            best_list.remove(split_list[i][2])
else:
    print('Only on trio with max priority exists (third_priority): ', third_priority)
    # TODO this is dead and for now needed to be updated

print('UPD best list (best_list): ', best_list)
problem_elements.clear()
for i in range(1, len(best_list) - 1):
    if ((best_list[i] - best_list[i + 1]) == -1) or ((best_list[i - 1] - best_list[i]) == -1):
            problem_elements.append(best_list[i])

if best_list[len(best_list) - 1] - best_list[len(best_list) - 2] == 1:
    problem_elements.append(best_list[len(best_list) - 1])

print('UPD List of positions of problem elements (problem_elements): ', problem_elements)
# Trying to add resolvment for new problem list
if len(problem_elements) > 1:
    for i in problem_elements:
        if (copy_list_planets[i-1] + copy_list_planets[i + 1]) > (copy_list_planets[i]):  # TODO to make universal as no such element present as there is only 1 in last section
            best_list.remove(i)             #TODO in previous if it actually should be like this "> (copy_list_planets[i] + split_list[i + 2])"
            break
        else:
            best_list.remove(i+1)
print('UPD Best planets to visit (best_list): ', best_list)
#TODO this is kastyl' try to rewrite
#best_list.reverse()
addition_to_best_list = []
for i in range(0, len(best_list)-1):
    if not best_list.count(best_list[i] + 2):
        addition_to_best_list.append(best_list[i]+2)
best_list = best_list + addition_to_best_list
result = 0
for i in best_list:
    result += copy_list_planets[i]
print('Result (result): ', result)
