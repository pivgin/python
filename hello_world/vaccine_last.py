import sys

input_param_w_list = sys.argv[1]
list_of_planets = []
temp_list_planets = []
temp_string = ''
temp_string_2 = ''
for i in range(0, len(input_param_w_list)):
    if input_param_w_list[i] == '[' or input_param_w_list[i] == ']' or input_param_w_list[i] == '-':
        continue
    else:
        temp_list_planets.append(input_param_w_list[i])
for i in temp_list_planets:
    temp_string += i
temp_string_2 = temp_string.split(',')
for i in temp_string_2:
    list_of_planets.append(int(i))
# Not in the mood to do validation of input command line params
# Program itself
copy_list_planets = list_of_planets.copy()
split_list = []
problem_elements = []
best_list = []
if len(list_of_planets) == 1:
    result = list_of_planets[0]
else:
    condition = True
    while condition:
        # Splitting list into trios
        split_list.clear()
        problem_elements.clear()
        best_list.clear()
        for i in range(0, len(copy_list_planets), 3):
            split_list.append(copy_list_planets[i: i+3])
        # Finding best elements in trios
        last_list_position = len(split_list)-1
        last_list = []
        last_list = split_list[last_list_position].copy()
        while len(last_list) < 3:
            last_list.append(0)
            split_list[len(split_list)-1].append(0)
        increment = 0
        for j in range(0, len(split_list)):
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
        # Finding sums in trios and finding problem elements from best_list
        sum_in_trios = []
        temp_sum = 0
        for i in range(0, len(split_list)):
            temp_sum = int(split_list[i][0] + split_list[i][2])
            if temp_sum > split_list[i][1]:
                sum_in_trios.append(temp_sum)
            else:
                sum_in_trios.append(split_list[i][1])
        # Preparing problem_list
        problem_elements.clear()
        for i in range(1, len(best_list)-1):
            if ((best_list[i] - best_list[i+1]) == -1) or ((best_list[i-1] - best_list[i]) == -1):
                problem_elements.append(best_list[i])
        if best_list[len(best_list)-1] - best_list[len(best_list)-2] == 1:
            problem_elements.append(best_list[len(best_list) - 1])
        # Resolving problem elements
        trios_w_problems = []
        for i in problem_elements:
            trios_w_problems.append(i//3)
        trios_w_problems = list(set(trios_w_problems))
        # Calculate sum in problem trios
        temp_sum = 0
        sum_in_trios.clear()
        for i in trios_w_problems:
            temp_sum = int(split_list[i][0] + split_list[i][2])
            if temp_sum > split_list[i][1]:
                sum_in_trios.append(temp_sum)
            else:
                sum_in_trios.append(split_list[i][1])
        first_trio_to_start = -1
        max_sum_in_trios = []
        max_sum_in_trios = [n for n, m in enumerate(sum_in_trios) if m == max(sum_in_trios)]
        if len(max_sum_in_trios) > 1:
            for i in range(0, len(max_sum_in_trios)-1):
                if max_sum_in_trios[i+1] - max_sum_in_trios[i] == 1:
                    first_trio_to_start = max_sum_in_trios[i]
        elif len(max_sum_in_trios) == 0:
            break
        else:
            first_trio_to_start = trios_w_problems[int(max_sum_in_trios[0])]
        if first_trio_to_start == len(split_list) - 1:
            if split_list[first_trio_to_start][1] + split_list[first_trio_to_start - 1][2] < split_list[first_trio_to_start][0] + split_list[first_trio_to_start-1][1]:
                split_list[first_trio_to_start - 1][2] = 0
                split_list[first_trio_to_start][1] = 0
            elif split_list[first_trio_to_start][1] + split_list[first_trio_to_start - 1][2] > split_list[first_trio_to_start][0] + split_list[first_trio_to_start-1][1]:
                split_list[first_trio_to_start][0] = 0
                split_list[first_trio_to_start-1][1] = 0
            else:
                if split_list[first_trio_to_start-1][2] > split_list[first_trio_to_start][0]:
                    split_list[first_trio_to_start][0] = 0
                    split_list[first_trio_to_start - 1][1] = 0
                else:
                    split_list[first_trio_to_start - 1][2] = 0
                    split_list[first_trio_to_start][1] = 0
        else:
            if split_list[first_trio_to_start][1] + split_list[first_trio_to_start+1][0] > split_list[first_trio_to_start+1][1] + split_list[first_trio_to_start][2]:
                split_list[first_trio_to_start][2] = 0
                split_list[first_trio_to_start + 1][1] = 0
            elif split_list[first_trio_to_start][1] + split_list[first_trio_to_start+1][0] < split_list[first_trio_to_start + 1][1] + split_list[first_trio_to_start][2]:
                split_list[first_trio_to_start][1] = 0
                split_list[first_trio_to_start + 1][0] = 0
            else:
                if split_list[first_trio_to_start][2] >= split_list[first_trio_to_start + 1][0]:
                    split_list[first_trio_to_start][1] = 0
                    split_list[first_trio_to_start + 1][0] = 0
                else:
                    split_list[first_trio_to_start][2] = 0
                    split_list[first_trio_to_start + 1][1] = 0
        copy_list_planets.clear()
        for i in split_list:
            for j in i:
                copy_list_planets.append(j)
        if len(problem_elements) <= 1:
            break
    result = 0
    for i in best_list:
        result += copy_list_planets[i]
list_even = []
list_odd = []
sum_even = 0
sum_odd = 0
final_result = 0
for i in range(0, len(list_of_planets)):
    if i % 2 == 0:
        list_even.append(list_of_planets[i])
    else:
        list_odd.append(list_of_planets[i])
for i in list_even:
    sum_even = sum_even + i
for i in list_odd:
    sum_odd = sum_odd + i
temp_list = [sum_odd, sum_even, result]
print(max(temp_list))

