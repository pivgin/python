#
# print("Hello World");
# print(3+5*8-10/5);
#
# birth_year = '1992'
# print(type(birth_year))
# period = 25
# print(type(period))
#
#
#
# print()
# print('Concatination in print int + str and convertion to diff types')
# print('------------||------------')
#
# print(1)
# print(int(birth_year) + period)
#
# print(2)
# print(str(period)+birth_year)
#
#
#
# print()
# print('Print functionality, separators and ending of string. Default output ending is /n ')
# print('------------||------------')
#
# print(birth_year, period)
# print(birth_year, period, sep='--fck--')
# print(birth_year, period, end='/n')             #default output ending
# print('--new line--')
# print()
# print(birth_year, period, end='--end_of_the_line--')
# print('--new line--')                           #watch output, intresting
# print('some text')
# print('some more text')
#
#
#
#
# print()
# print('Input functionality. Result is always string (str)')
# print('------------||------------')
# input_text = input('Please enter some text: ')          #result will be always string (str)
# print()
# print('User entered next value: ', input_text)
#
# print('Testing that result type of input is always str')
# name = input('Enter your name: ')
# print(type(name))
# #str
# age = input('Enter your age: ')
# print(type(age))
# #str
# true_value = input('Do you like python: ')              #True or False is expected
# print(type(true_value))
# # the result is always string (str)
#
#
#
# print()
# print('Math operations')
# print('------------||------------')
# age = int(input('Your age: '))
# average_age = 64
# population = 10000000
# years_left = average_age - age
# print('Years left: ', years_left)
# all_people_live = population * average_age
# print('All people lived for: ', all_people_live)
# live_part = age / average_age
# print('You live ', live_part, 'of average live cycle')
# print(type(live_part))
# # About / (devision)
# # / - simple division, float as a result
# # // - integer(whole) part of division
# # % - reminder of the division
# # ** - exponentiation
#
# # Boolean as a result
# # == equals
# # != not equals
# # <, >, <=, >=
#
# # and, or, not - Logical operands
#
#
# print()
# print('Condition operators')
# print('------------||------------')
# if age > average_age :
#     print ('You are lucky to live!')
# elif age == average_age:
#     print('You are ready to die')
# else:
#     print('You will leave atleast ', average_age - age, ' years more')
# # else, if, elif
#
#

print()
print('break, continue, while-else')
print('------------||------------')

name = None
while True:
    name = input('YES?')
    if name == 'YES':
        break
    print('Your are not correct!')
print ('You are correct')


number = 0
n = int(input('Number: '))
while number < n:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1

number = 0
while number <= 100:
    print(number)
    number += 1
    if number == 33:
        break
else:                           # will work only if cycle ended by condition
    print("else ---- end")
print('end')

