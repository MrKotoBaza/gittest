print("Конвертер величин")
print("Воспринимаемые величины:")
tOVL = ['км', 'м', "см"]
tOVM = ['кг', "г", "мг"]
typesOfValues= ['км', 'м', 'кг', "г", "см", "мг"]
for i in typesOfValues:
    print (i)
while True:
    c = 0
    typeOfVal =  input("Какова величина введенного значения?: ")
    val = int(input("Введите само значение (число): "))
    tf = input("В какую величину вы хотите перевести значение?: ")
    if val == 0:
        print('Неправильное значение')
    else:
        if typeOfVal != tf:
            if typeOfVal in tOVL and tf in tOVL:
                if typeOfVal == "м" and tf == "см" or typeOfVal == "м" and tf == "км":
                    c = val*1000 
                if typeOfVal == "см" and tf == "м" or typeOfVal == "км" and tf == "м":
                    c = val/1000 
                if typeOfVal == "см" and tf == "км":
                    c = val /1000000 
                if typeOfVal == "км" and tf == "см":
                    c = val*1000000 
                if typeOfVal == "см":
                    c = c/10
                if tf == "см":
                    c = c*10
                print("{0}{1} = {2}{3}".format(val, typeOfVal, c, tf))
            elif typeOfVal in tOVM and tf in tOVM:
                if typeOfVal == "мг" and tf == "г" or typeOfVal == "г" and tf == "кг":
                    c = val/1000 
                if typeOfVal == "г" and tf == "мг" or typeOfVal == "кг" and tf == "г":
                    c = val*1000 
                if typeOfVal == "мг" and tf == "кг":
                    c = val/ 1000000 
                if typeOfVal == "кг" and tf == "мг":
                    c = val*1000000 
                print("{0}{1} = {2}{3}".format(val, typeOfVal, c, tf))
            else:
                print("Неверные значения величин!")
        else:
            print("Неверные значения величин!")
        

        

        
