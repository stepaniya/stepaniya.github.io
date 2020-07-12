import random


def random_number():
    while True:
        popitci = 10
        game_popitci = 0
        bot_number = random.randint(1, 25)
        while True:
            game_number = input('Введи число:')
            if game_number.isdigit():
                if int(game_number) >= 1 and int(game_number) <= 25:
                    if int(game_number) > bot_number:
                        print('Твоё число больше чем загадоное ')
                        game_popitci += 1
                        print('Число попыток:', game_popitci)

                    elif int(game_number) < bot_number:
                        print('Твоё число менше чем загадоное ')
                        game_popitci += 1
                        print('Число попыток:', game_popitci)

                    elif int(game_number) == bot_number:
                        print('Ты выиграл ')
                        print('Число попыток:', game_popitci)
                        game_popitci = 0
                        bot_number = random.randint(1, 25)
                        continue

                    if game_popitci == popitci:
                        print('Ты проиграл ')
                        print('Число бота:', bot_number)
                        print('Число попыток:', game_popitci)
                        game_popitci = 0
                        bot_number = random.randint(1, 25)
                        continue
                else:
                    print('Что ты ввел')
            else:
                print('Что ты ввел')



print(random_number())
