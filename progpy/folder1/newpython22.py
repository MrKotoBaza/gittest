print("Вовзведение в степень числа до определенного предела")
i = 1
p = int(input("Введите число для возведения степень: "))
n = int(input("Введите ограничение: "))
while i**p <n:
    print(i**p)
    i+=1