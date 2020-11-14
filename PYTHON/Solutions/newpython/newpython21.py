print("Вывод числа, обратного введенному по порядку составляющих его цифр")
num1 = input("Введите число для переворота: ")
decomposition = []
b = ''
for i in num1:
    print(i)
    b = i + b
    print(b)
print(b)