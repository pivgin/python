# 1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран. Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
# 2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.
# 3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
#
#     Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
#     Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
#     Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
#
#     Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
#     (Формула не соответствует реальной действительности и здесь используется только ради примера)
#
#     Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно. В случае ошибок, уточните условия для той или иной ситуации.
#
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

print('---------||---------')
print('task_1 user number + 2')
user_number = int(input('Input number: '))
print('Result number is: ', user_number + 2)
print()

print('---------||---------')
print('task_2 request number less than 10 but greater than 0 in cycle')
user_number = 0
while user_number <= 0 or user_number >= 10:
    user_number = int(input('Input number: '))
    if user_number <= 0 or user_number >= 10:
        print('This number is invalid')
        print('Correct diapason is in between 0 and 10 not included')
        print('Please try again')
print(user_number, ' is correct number. Result number is ', user_number**2)
print('End of the programm')
print()

print('---------||---------')
print('task_3 Medical survey')
name = input('Your First Name: ')
surname = input('Your Last Name: ')
age = int(input('Your age: '))
weight = int(input('Your weight: '))
temp_value = 0
#if 50 > weight > 120:
if age <= 30 and 50 <= weight <= 120:
    print(name, ' ', surname, ', Your condition is good')
elif weight < 50 or weight > 120:
    if age >= 40:
        print(name, ' ', surname, ', You need a doctor')
    elif age < 40 and age > 30:
        print(name, ' ', surname, ', More sports needed')
    else:
        print(name, ' ', surname, ', You are to young to think about your health!!!!')
else:
     print(name, ' ', surname, ', You do not belong to our survey')
print('The End')
