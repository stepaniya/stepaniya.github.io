import random
import os


while True:

    bot_number_hard = random.randint(1, 100)
    bot_number_normal = random.randint(1, 50)
    bot_number_eazy = random.randint(1, 25)
    chislo_popitoc = 0


    def random_number(chislo_popitoc):
        if slochnost == 1:
            bot_number = bot_number_eazy
        if slochnost == 2:
            bot_number = bot_number_hard
        if slochnost == 3:
            bot_number = bot_number_hard
        while True:
            game_number = input('Введи число:')
            if int(game_number) > bot_number:
                print('Твоё число больше чем загадоное:')
                chislo_popitoc += 1
                print('Число попыток:', chislo_popitoc)

            elif int(game_number) < bot_number:
                print('Твоё число менше чем загадоное:')
                chislo_popitoc += 1
                print('Число попыток:', chislo_popitoc)

            elif int(game_number) == bot_number:
                print('Ты выиграл ')
                print('Число попыток:', chislo_popitoc)
                break

            if chislo_popitoc == popitci:
                print('Ты проиграл')
                print('Число попыток:', chislo_popitoc)
                break


    slochnost = int(input('Введи сложность игры 1(1,25) / 2(1,50) / 3(1,100): '))
    popitci = int(input('Число попыток:'))
    os.system('cls')
    print(random_number(chislo_popitoc))
    igra = input('Хочешь сыграть ещё + / если не то - :')
    if igra == '+':
        os.system('cls')
        continue
    if igra == '-':
        break
