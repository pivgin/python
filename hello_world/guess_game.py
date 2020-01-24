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
max_tries = 5
#print(number)
while input_number != number:
    tries += 1
    if tries > max_tries:
        print('You are looser!')
        break
    print('{}th try'.format(tries))
    input_number = int(input('Please input number'))
    if input_number > number:
        print('Go lower')
    elif input_number < number:
        print('Go higher')
else:
    print('You tried {} times'.format(tries))
    print('Congrats! {} is correct number!'.format(input_number))



