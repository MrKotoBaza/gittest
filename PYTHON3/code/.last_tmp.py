import random
import numpy
def trunk(c):
    string = " "*(c-1) + "|" + " |"
    return string
x = int(input("Введите высоту ели в строках: "))
if x < 4:
    count = 0
elif x >= 4 and x < 15:
    count = 1
else: 
    count = 2

xs = x
temp = " " #строка елки
stars= 1 #счетчик количества звезд, что используются в создании строки елки

while xs>0:
    if stars == 1:
        temp = " "*xs + "☆" #первый ряд елки использует только значок звезды
    else:
        n = random.randint(1, stars)
        temp = " "*xs + "*"*(n-1) + "\xA4" +"*"*(stars-n) #строка елки = "отступу в пробелах" + "звездочки перед елочной игушкой" + "сама игрушка" + "оставшиеся игрушки"
    print(temp)
    xs-=1
    stars +=2
while count >0:
    print(trunk(x)) #функция trunk() создает ствол дерева (с условиями высоты елки, если меньше 4, ствола нет вообще, если больше 4, ствол в одну строку высотой, если больше 15, ствол высотой в две строки)
    count-=1
print("-"*stars)