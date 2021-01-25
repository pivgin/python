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
list_of_planets = [5, 2, 4, 3, 5, 6, 2, 2, 2]           # TODO this example does not work
# list_of_planets = [4, 4, 4, 3, 3, 3, 5, 5, 5]             # TODO this example does not work
# list_of_planets = [4, 8, 5, 2]
# list_of_planets = [4, 2, 3, 4]
# list_of_planets = [5, 2, 4, 3, 5, 6, 2]
print(list_of_planets)
copy_list_planets = list_of_planets.copy()
# Splitting list into trios
split_list = []
problem_elements = []
best_list = []
condition = True
while condition:
    split_list.clear()
    problem_elements.clear()
    best_list.clear()
    for i in range(0, len(copy_list_planets), 3):
        split_list.append(copy_list_planets[i: i+3])
    print('Split list by 3 elements (split_list): ', split_list)
    # Finding best elements in trios
    last_list_position = len(split_list)-1
    last_list = []
    # creating copy of last section of planets
    last_list = split_list[last_list_position].copy()
    while len(last_list) < 3:
        last_list.append(0)
        split_list[len(split_list)-1].append(0)
    increment = 0
    for j in range(0, len(split_list)-1):
        if split_list[j][0] + split_list[j][2] > split_list[j][1]:
            if split_list[j][0] == 0:
                best_list.append(2 + increment)
            elif split_list[j][2] == 0:
                best_list.append(0 + increment)
            else:
                best_list.append(0+increment)
                best_list.append(2+increment)
        else:
            best_list.append(1+increment)
        increment += 3
    # Checking last section of initial list of planets
    # last_list_position = len(split_list)-1
    # last_list = []
    # # creating copy of last section of planets
    # last_list = split_list[last_list_position].copy()
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
    print('Problem list: ', problem_elements)
    # Preparing problem_list
    problem_elements.clear()
    for i in range(1, len(best_list)-1):
        if ((best_list[i] - best_list[i+1]) == -1) or ((best_list[i-1] - best_list[i]) == -1):
            problem_elements.append(best_list[i])
    if best_list[len(best_list)-1] - best_list[len(best_list)-2] == 1:
        problem_elements.append(best_list[len(best_list) - 1])
    print('List of positions of problem elements (problem_elements): ', problem_elements)
    # Resolving problem elements
    trios_w_problems = []
    for i in problem_elements:
        trios_w_problems.append(i//3)
    trios_w_problems = list(set(trios_w_problems))
    # Calculate sum in problem trios
    temp_sum = 0
    sum_in_trios.clear()
    for i in trios_w_problems:                   # TODO looks like problem. Needed to be rewritten to check only problem sections
        if len(split_list[i]) == 1:
            sum_in_trios.append(split_list[i][0])
        elif len(split_list[i]) == 2:
            sum_in_trios.append(max(split_list[i]))
        else:
            temp_sum = int(split_list[i][0] + split_list[i][2])
            if temp_sum > split_list[i][1]:
                sum_in_trios.append(temp_sum)
            else:
                sum_in_trios.append(split_list[i][1])
    print('List of max possible sums in sections of planets (sum_in_trios): ', sum_in_trios)
    # if len(split_list) != len(sum_in_trios):
    # TODO sum_in_trios list does not show all the trios sums so that position of max_sum_in_trios si not correct
    first_trio_to_start = -1
    max_sum_in_trios = []
    max_sum_in_trios = [n for n, m in enumerate(sum_in_trios) if m == max(sum_in_trios)]
    print('Positions of best trios (max_sum_in_trios):', max_sum_in_trios)
    if len(max_sum_in_trios) > 1:
        for i in range(0, len(max_sum_in_trios)-1):
            if max_sum_in_trios[i+1] - max_sum_in_trios[i] == 1:
                first_trio_to_start = max_sum_in_trios[i]
    elif len(max_sum_in_trios) == 0:
        break
    else:
        # first_trio_to_start = sum_in_trios.index(max(sum_in_trios))
        first_trio_to_start = trios_w_problems[int(max_sum_in_trios[0])]
        # first_trio_to_start = trios_w_problems.pop()
    print('First trio to start is (first_trio_to_start): ', first_trio_to_start)
    print('Split list: ', split_list)
    # TODO полное дерьмо, нихера эта логика не работает
    if split_list[first_trio_to_start][1] + split_list[first_trio_to_start+1][0] > split_list[first_trio_to_start+1][1] + split_list[first_trio_to_start][2]:
        split_list[first_trio_to_start][2] = 0
        split_list[first_trio_to_start + 1][1] = 0
    elif split_list[first_trio_to_start][1] + split_list[first_trio_to_start+1][0] < split_list[first_trio_to_start+1][1] + split_list[first_trio_to_start][2]:
        split_list[first_trio_to_start][1] = 0
        split_list[first_trio_to_start +1][0] = 0
    else:
        if split_list[first_trio_to_start][2] >= split_list[first_trio_to_start + 1][0]:
            split_list[first_trio_to_start][1] = 0
            split_list[first_trio_to_start + 1][0] = 0
        else:
            split_list[first_trio_to_start][2] = 0
            split_list[first_trio_to_start + 1][1] = 0
    print('UPD split_list: ', split_list)
    print(problem_elements)
    # Searching for new sums and problem elements
    copy_list_planets.clear()
    for i in split_list:
        for j in i:
            copy_list_planets.append(j)
    print(copy_list_planets)
    print('-------------------------End of cycle----------------------')
    if len(problem_elements) <= 1:
        break
# print('Last problem elements (problem_elements): ', problem_elements)
result = 0
for i in best_list:
    result += copy_list_planets[i]
print('Result (result): ', result)
# Cheat cycle
list_chet = []
list_nechet = []
sum_chet = 0
sum_nechet = 0
final_result = 0
for i in list_of_planets:
    if i % 2 == 0:
        list_chet.append(i)
    else:
        list_nechet.append(i)
for i in list_chet:
    sum_chet = sum_chet + i
for i in list_nechet:
    sum_nechet = sum_nechet + i
temp_list = [sum_nechet, sum_chet, result]
print(max(temp_list))
# if sum_chet >= sum_nechet and sum_chet >= result:
#     final_result = sum_chet
# elif sum_chet

