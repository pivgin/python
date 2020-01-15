# print()
# print('Lesson_4 Strings')
# print('------------||------------')
# print()
# print()
#
# print('Basics')
# print('------------||------------')
# friend = 'Maxim'
# print(type(friend))
# # type is str
#
# friend = "Maxim"
# print(type(friend))
# # type is str
#
# say  = 'say "Hello"'
# print(say)
# # It is ok to use differrent '" but should be paired
# # output - say "Hello"
# print()
#
# print('Index')
# print('------------||------------')
# print()
# first_letter = friend[0]
# print('First letter is - ', first_letter)
# print('Type of first symbol is also string', type(first_letter))
# # string is actually kinda massive of strings
#
# first_letter = friend[-1]
# print('First letter is - ', first_letter)
# # index can be negative, so the letter from the end
# print()
#
# print('Cut')
# print('------------||------------')
# print()
# friend = 'Maxim'
# # from 1 till 4
# print(friend[1:4])
# # from beginning till 4
# print(friend[:4])
# # from 3 till the end
# print(friend[3:])
# # type of cut is STR
# print(type(friend[1:2]))
# print()
#
# print('Functions with strings')
# print('------------||------------')
# print()
# # len(str) - lenght
# # friend.find('a') - finding of a in string
#
# friends = "Maxim Leonard"
# print(friends)
# print(len(friends))
# print(friends.find('ax'))
# # result 1, so it is the begining index
# print(friends.find('1ax'))
# # result is -1, so no string found
# print(friends.split())
# # default devision is SPACE, so the result LIST of 2 strings
# friends = "Maxim/Leonard"
# print(friends.split('/'))
# # will by split by /, result is still LIST
# print(friends.isdigit())
# # if string consists only from digits, result BOOLEAN
# number = '123456'
# print(number.isdigit())
# # True
# number2 = '1234r567'
# print(number2.isdigit())
# # False
# print(friends.upper())
# # convert to upper
# print(friends.lower())
# # convert to lower
# print()
#
# print('Formating strings')
# print('------------||------------')
# print()
# name = 'Max'
# age = 27
# # 1. concatination (bad cause hard to readcode and variables should be of correct type)
# hello_srt = 'Hi, ' + name + ' you are ' + str(age) + ' years old'
# print(hello_srt)
# # 2. % - more readable but still type of variables
# hello_srt = 'Hi, %s you are %d years old'%(name, age)
# print(hello_srt)
# # 3. format - the best one, no vars types
# hello_srt = 'Hi, {} you are {} years old'.format(name, age)
# print(hello_srt)
# print()
#
# print('Lists')
# print('------------||------------')
# print()
# empty_list = []
# friends = ['Mick', 'Leo', 'Raff']
# print(type(friends))
# # <class 'list'>
# print('1st ', friends[1])
# print('Last ', friends[-1])
#
# print(friends[1:2])
#
#
# print(len(friends))
# # lenght of listm result 3
# print(friends.append('Don'))
# # adding new element
# print(friends.pop())
# # removes last element and collect it
# friends.clear()
# # clear whole list, making empty
# friends = ['Mick', 'Leo', 'Raff']
# print(friends.remove('Leo'))
# # removes elements by values
# print(friends)
# del friends[0]
# print(friends)
# # remove element by index
# print()
#
# print('List operators. Operator IN')
# print('------------||------------')
# print()
# hero = 'Superman'
# if hero.find('man') != -1:
#     print('Yes')
#
# if 'man' in hero:
#     print('Yes')
#
# friends = ['Mick', 'Leo', 'Raff']
# if 'Leo' in friends:
#     print('Cavabanga')
# print()
#
#
# print('Tuple type')
# print('------------||------------')
# print()
# # not changable list
# roles = ('user', 'admin', 'manager')
# print()
#
#
# print('Example of lesson')
# print('------------||------------')
# print()
# print('Python')
# count = int(input('Number of participants: '))
# i = count
# members = []
# while i > 0:
#     name = input('who is on {} place'.format(i))
#     members.append(name)
#     i -= 1
#
# print(sorted(members), ' took place in comp')
# members.reverse()
# result = members[:3]
# result = 'Winners are {}. Congrats!'.format(result)
# print(result)
# print()
#
#
# print('For in cycle. progressions')
# print('------------||------------')
# print()
# friend_name = "Raff"
# friends = ["Mick", "Raff", "Don", "Leo"]
# roles = ('admin', 'user', 'manager')
# # for
# for friend in friends:
#     print(friend)
# print()
#
# # while
# i = 0
# while i < len(friends):
#     friend = friends[i]
#     print(friend)
#     i += 1
# print()
#
# # for string
# for letter in friend_name:
#     print(letter)
# print()
#
# # for tuple
# for role in roles:
#     print(role)
# print()
#
#
#
# print('Range function')
# print('------------||------------')
# print()
# # progression of natural numbers, used with for cycle
# # used to create range of numbers (number of numbers = n) from 0 till n-1
# numbers = range(10)
# print(numbers)
# print(type(numbers))
# # range(0, 10)
# # <class 'range'>
# print(list(numbers))
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print()
#
# turtles = ['Raff', 'Mick', 'Don']
# # simple for
# for ninja in turtles:
#     print(ninja)
# print()
# # range
# for i in range(len(turtles)):
#     print(i, ')', turtles[i])
# print()
#
# # range(start_or_stop, stop[, step])
# # start_or_stop - beginning or end of progression
# # stop - end
# # step - step
#
# print(list(range(1,1000,2)))
# print()
#
# for number in range(1, 1000, 2):
#     print(number)
# print()
#
#
# print('Dictionary')
# print('------------||------------')
# print()
# # my_dict = {key1:val1, key2:val2, ...}
# friend = {'name' : 'Leo', 'age': 23}
# print(friend)
# # {'name': 'Leo', 'age': 23}
# print(type(friend))
# # <class 'dict'>
# print()
# print(friend['age'])
# # 23
# friend['has_car'] = True
# print(friend)
# # {'name': 'Leo', 'age': 23, 'has_car': True}
# friend['has_car'] = False
# print(friend)
# # {'name': 'Leo', 'age': 23, 'has_car': False}
# # so adding if new, replace if already exist
#
# del friend['age']
# print(friend)
# # {'name': 'Leo', 'has_car': False}
# print()
#
# if 'age' in friend:
#     print('Exist')
# # no out, cause does not exist
# print()
#
# if 'has_car' in friend:
#     print('Exist')
# # Exist
# print()
#
#
# friend = {'name': 'Leo', 'age': 23, 'has_car': True}
# # only keys
# for key in friend.keys():
#     print(key)
#     print(friend[key])
# # name
# # Leo
# # age
# # 23
# # has_car
# # True
# print()
#
# for key in friend:
#     print(key)
#     print(friend[key])
# # same
# print()
#
# # only values
# for val in friend.values():
#     print(val)
# # Leo
# # 23
# # True
# print()
#
# # both key and value
# for item in friend.items():
#     print(item)
# # ('name', 'Leo')
# # ('age', 23)
# # ('has_car', True)
# # so like tuple
# print()
#
# for key, val in friend.items():
#     print(key)
#     print(val)
# # name
# # Leo
# # age
# # 23
# # has_car
# # True
# print()
#
#
#
# print('Sets')
# print('------------||------------')
# print()
# # cannot be two equal elements
# # cities = {'Minsk', 'Moscow', 'Vilnius', 'Paris'}
#
# cities_1 = {'Minsk', 'Moscow', 'Vilnius', 'Moscow', 'Paris'}
# print(type(cities_1))
# # <class 'set'>
# print(cities_1)
# # {'Vilnius', 'Moscow', 'Paris', 'Minsk'}
# print()
#
# cities = ['Minsk', 'Moscow', 'Vilnius', 'Moscow', 'Paris']
# print(type(cities))
# # <class 'list'>
# print(cities)
# # ['Minsk', 'Moscow', 'Vilnius', 'Moscow', 'Paris']
# print()
#
# cities = set(cities)
# print(cities)
# # {'Moscow', 'Paris', 'Minsk', 'Vilnius'}
# print(type(cities))
# # <class 'set'>
# print()


print('Actions with sets')
print('------------||------------')
print()
# cities.add('Burma')
# cities.remove('Moscow')
# len
# operator IN and cycle for
# actions with some sets (grouping, etc...)
cities = {'Minsk', 'Moscow', 'Vilnius', 'Paris'}
print(cities)
cities.add('Burma')
print(cities)
cities.add('Minsk')
print(cities)
# Can't be added as already exist in set
print()
cities.remove('Moscow')
print(cities)
print(len(cities))
# 4
print()
print('Paris' in cities)
# True
for city in cities:
    print(city)
print()



print('Actions with sets (&, |, -)')
print('------------||------------')
print()
raff_things = {'Razor', 'Shorts', 'T-short', 'Phone'}
mick_things = {'Phone', 'Umbrella', 'Lipstick', 'Shorts'}
# all things w/o equals
print(raff_things | mick_things)
#{'Phone', 'Razor', 'Umbrella', 'Lipstick', 'T-short', 'Shorts'}

# things in common
print(raff_things & mick_things)
# {'Phone', 'Shorts'}

# not raff but mick
print(raff_things - mick_things)
# {'T-short', 'Razor'}

# not mick but raff
print(mick_things - raff_things)
# {'Lipstick', 'Umbrella'}




#18:15