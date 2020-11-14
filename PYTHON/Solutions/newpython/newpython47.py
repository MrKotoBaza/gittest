s = input()
num1 = 0
num2 = 0
for i in range(0, 3):
    num1+= int(s[i])
for i in range(3, 6):
    num2+= int(s[i])
if num1 == num2:
    print("Счастливый")
else:
    print("Обычный")
