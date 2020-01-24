# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.

import random
print('Game_guess_the_number.')
print('------------||------------')
print()
number = random.randint(1, 100)
input_number = 0

tries = 0
levels = {1: 15, 2: 10, 3: 5, 4: 3, 5: 1}
level = int(input('Please select the level (from 1 till 5 where 5 is hardest): '))
max_tries = levels[level]

users_count = int(input('Input number of users: '))
users = []
for i in range(users_count):
    user_name = input('Input name for user {}: '.format(i))
    users.append(user_name)
print(users)
#print(number)

is_winner = False
winner_name = None

while not is_winner:
    tries += 1
    if tries > max_tries:
        print('All users are loosers!')
        break
    print('{}th try'.format(tries))
    for user in users:
        print('{} user turn'.format(user))
        input_number = int(input('Please input number'))
        if input_number == number:
            is_winner = True
            winner_name = user
            break
        elif input_number > number:
            print('Go lower')
        else:
            print('Go higher')
else:
    print('You tried {} times'.format(tries))
    print('Congrats, {}! {} is correct number!'.format(winner_name, input_number))



