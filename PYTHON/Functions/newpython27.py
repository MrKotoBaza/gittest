def nok(a, b):
    m = a*b
    while a!= 0 and b != 0:
        if a>b:
            a%=b
        else:
            b%=a

    return m/(a+b)

while 1:
    try:
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))
        print("Их НОК равен ",int(nok(x, y)))
    except:
        break


