def helpp():
    print("-"*20)
    print("Я могу использовать такие значения:")
    for i in range (0, 8):
        print("{} - {}".format(typesOfValues[i], shortTypes[i]))
    print("Для правильного использования вводи в меня виды значений также, как и в первом столбце,\n и я выдам тебе ответ!")
    print("Не забывай, 0=0")
    print("-"*20)
    
print("Конвертер величин")
print("Поддерживаемые величины: ")
typesOfValues = ["Километры","Метры","Дециметры","Сантиметры","Килограммы","Граммы","Милиграммы","Тонны"]
shortTypes = ["км","м","дм","см","кг","г","мг","т"]
for i in range (0, 8):
    print("{} - {}".format(typesOfValues[i], shortTypes[i]))
while True:
    print("Введите сначала из какой величины в какую надо переводить значение, а после - само значение")
    print("/help для получения справки")
    string = input("Что во что?: ")
    val = float(input("Сколько? "))

    string = string.split(" в ")
    if len(string) == 2:
        string[0] = string[0].lower()
        string[1] = string[1].lower()
    else:
        string.append(" ")

    if string[0] == "километры":
        if string[1]=="метры":
            print(val, "км", "=", val*1000, "м")
        elif string[1]=="сантиметры":
            print(val, "км", "=", val*100000, "см")
        elif string[1]=="дециметры":
            print(val, "км", "=", val*10000, "дм")
        else:
            print("Not right value of types")
    elif string[0] == "метры":
        if string[1]=="километры":
            print(val, "м", "=", val/1000, "км")
        elif string[1]=="сантиметры":
            print(val, "м", "=", val*100, "cм")
        elif string[1]=="дециметры":
            print(val, "м", "=", val*10, "дм")
        else:
            print("Not right value of types")
    elif string[0] == "сантиметры":
        if string[1]=="метры":
            print(val, "cм", "=", val/100, "м")
        elif string[1]=="километры":
            print(val, "cм", "=", val/100000, "км")
        elif string[1]=="дециметры":
            print(val, "cм", "=", val/10, "дм")
        else:
            print("Not right value of types")
    elif string[0] == "дециметры":
        if string[1]=="метры":
            print(val, "дм", "=", val/10, "м")
        elif string[1]=="сантиметры":
            print(val, "дм", "=", val*10, "см")
        elif string[1]=="километры":
            print(val, "дм", "=", val/10000, "км")
        else:
            print("Not right value of types")
    elif string[0]=="тонны":
        if string[1]=="килограммы":
            print("т", val, "=", val*1000, "кг")
        elif string[1]=="граммы":
            print("т", val, "=", val*1000000, "г")
        elif string[1]=="милиграммы":
            print("т", val, "=", val*1000000000, "мг")
        else:
            print("Not right value of types")
    elif string[0]=="килограммы":
        if string[1]=="тонны":
            print("кг", val, "=", val/1000, "т")
        elif string[1]=="граммы":
            print("кг", val, "=", val*1000, "г")
        elif string[1]=="милиграммы":
            print("кг", val, "=", val*1000000, "мг")
        else:
            print("Not right value of types")
    elif string[0]=="граммы":
        if string[1]=="килограммы":
            print("г", val, "=", val/1000, "кг")
        elif string[1]=="тонны":
            print("г", val, "=", val/1000000, "т")
        elif string[1]=="милиграммы":
            print("г", val, "=", val*1000, "мг")
        else:
            print("Not right value of types")
    elif string[0]=="милиграммы":
        if string[1]=="килограммы":
            print("мг", val, "=", val/1000000, "кг")
        elif string[1]=="граммы":
            print("мг", val, "=", val/1000, "г")
        elif string[1]=="тонны":
            print("мг", val, "=", val/1000000000, "т")
        else:
            print("Not right value of types")
    elif string[0]=="/help":
        helpp()
    else:
        print("Not right value of types")
#
# 
# 
# Сделать его на TKinter
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# #
