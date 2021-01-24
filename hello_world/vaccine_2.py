print('Rick\'s vaccine')
print('------------||------------')
print()
# Asking for list of planets section
# TODO add input verification
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
list_of_planets = [5, 2, 4, 3, 5, 6, 2, 5, 2]
# list_of_planets_ = [4, 8, 5, 2]
# list_of_planets_ = [4, 2, 3, 4]
# list_of_planets_ = [5, 2, 4, 3, 5, 6, 2, 2]
print(list_of_planets)
copy_list_planets = list_of_planets.copy()
# Splitting list into trios
split_list = []
for i in range(0, len(copy_list_planets), 3):
    split_list.append(copy_list_planets[i: i+3])
print('Split list by 3 elements (split_list): ', split_list)
# Finding best elements in trios
best_list = []
increment = 0
for j in range(0, len(split_list)-1):
    if split_list[j][0] + split_list[j][2] > split_list[j][1]:
        best_list.append(0+increment)
        best_list.append(2+increment)
    else:
        best_list.append(1)
    increment += 3
# Checking last section of initial list of planets
last_list_position = len(split_list)-1
last_list = []
# creating copy of last section of planets
last_list = split_list[last_list_position].copy()
if len(last_list) == 1:
    best_list.append(0+increment)
elif len(last_list) == 2:
    max_last_list_positions = [n for n, m in enumerate(last_list) if m == max(last_list)]
    for i in max_last_list_positions:
        i += increment
        best_list.append(i)
else: #TODO can be added to trios verifications row but verification for number of elements in last list should be added before and if it is 3 than cycle should go through whole list
    if (last_list[0] + last_list[2] > last_list[1]):
        # TODO if sums are equal
        best_list.append(0+increment)
        best_list.append(2+increment)
    else:
        best_list.append(1+increment)
print('Positions of potentially best planets to visit (best_list): ', best_list)
# Finding sums in trios and finding problem elements form best_list
sum_in_trios = []
temp_sum = 0
for i in range(0, len(split_list)-1):                   # TODO looks like problem. Needed to be rewritten to check only problem sections
    temp_sum = int(split_list[i][0] + split_list[i][2])
    if temp_sum > split_list[i][1]:
        sum_in_trios.append(temp_sum)
    else:
        sum_in_trios.append(split_list[i][1])
if len(last_list) == 1:
    sum_in_trios.append(last_list[0])
elif len(last_list) == 2:
    sum_in_trios.append(max(last_list))
else:   #TODO not correct if lats trio has 3 elements as it is counted to sum of trios in previous cycle
    if (last_list[0] + last_list[2]) > (last_list[1]):
        sum_in_trios.append(last_list[0] + last_list[2])
    else:
        sum_in_trios.append(last_list[1])
print('List of max possible sums in sections of planets (sum_in_trios): ', sum_in_trios)

# trios_priority = sum_in_trios.index(max(sum_in_trios))
# # print(trios_priority)
# high_sum_in_trios = split_list[trios_priority]
# print('high_sum_in_trios: ', high_sum_in_trios)
# TODO add if verification for case with one max trio           almost done
first_trio_to_start = -1
max_sum_in_trios = []
max_sum_in_trios = [n for n, m in enumerate(sum_in_trios) if m == max(sum_in_trios)]
print('Positions of best trios (max_sum_in_trios):', max_sum_in_trios)
if len(max_sum_in_trios) > 1:
    for i in range(1, len(max_sum_in_trios)-1):
        if max_sum_in_trios[i] - max_sum_in_trios[i-1] == 1:
            first_trio_to_start = max_sum_in_trios[i-1]
else:
    first_trio_to_start = sum_in_trios.index(max(sum_in_trios))
print('First trio to start is (first_trio_to_start): ', first_trio_to_start)
# Preparing problem_list
problem_elements = []
for i in range(1, len(best_list)-1):
    if ((best_list[i] - best_list[i+1]) == -1) or ((best_list[i-1] - best_list[i]) == -1):
        problem_elements.append(best_list[i])
if best_list[len(best_list)-1] - best_list[len(best_list)-2] == 1:
    problem_elements.append(best_list[len(best_list) - 1])
print('List of positions of problem elements (problem_elements): ', problem_elements)
