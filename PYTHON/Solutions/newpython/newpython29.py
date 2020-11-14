import random
string = input("Что вы хотите выбрать? Впишите строкой с <<или>>")
string = string.split(" или ")

val = random.randint(0, 100)

if val%2 ==0:
    print(string[int(random.randint(0, 2))])
else:
    print(string[int(random.randint(0, 2))])

