print("Введите единицы измерения. в которые нужно перевести имеющиеся")
typ = str(input())
print("Введите само число")
num1=float(input())
num2=0
itis=""
if typ=="m":
    num2=num1/100
    itis="cm"
elif typ=="t":
    num2=num1/1000
    itis="kg"
print(f"Число {num1}, введенное в {itis}, в {typ} равно {num2}")

    