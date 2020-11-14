import random
record = 0

def globalCycle():
    global c
    global numRange 
    global inGame
    while inGame:

        numRange = random.randint(50, 1000)
        c = random.randint(1, numRange)
        print("Компьютер загадал число от 1 до", numRange)
        print("Если вы хотите выйти из игры - введите 0")
        print("Рекорд:", record)
        print("Ваши очки:", points)

        print("__________________________________________________________________________________________")

        cycle()

def cycle():
    global num
    global c
    global points
    global record
    global inGame
    global numRange
    while num != 0:
        num = int(input("Введите число от 1 до {}: ".format(numRange)))
        if num == c:
            print("Победа! Поздравляю!")
            points += 5
            record = points
            num = 1
            return
        elif num == 0:
            inGame = False
            points = 0
            num = 1
            return
        
        else:
            if num>c:
                print("Слишком много!")
            elif num<c:
                print("Слишком мало!")       

while True:
    num = 1
    inGame = True
    c = 0
    numRange = 0
    points = 0
    print("__________________________________________________________________________________________")
    print("Игра 'Угадай число'")
    print("Ваша цель - ушадать число, которое загадает компьютер!")
    go = input("Хотите играть? y/n: ")
    if go == "y":
        globalCycle()
    elif go == "n":
        break
    else:
        print("Invalid char")


