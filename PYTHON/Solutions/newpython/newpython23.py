print("Действие над 1 в определенной последовательности и складывание всех чисел последовательности")
do = input("Что делать с 1?: ")
n = int(input("Сколько чисел последовательности складывать?: "))
a = 1
do = "a = a"+do
i = 1
mas = []
mas.append(a)
summ = 1
while i<n:
    exec(do)
    summ+= a
    mas.append(a)
    i+=1
print(summ)
print('')
print('')
print(mas)