from math import pi
from math import ceil
print("Сколько банок надо для окраски поверхности?")
d = float(input("Введите диаметр дна бака: "))
h = float(input("Введите высоту бака"))
stainIn = input("Окрашивать ли внутри? Да-нет: ")
temp = float(input("На сколько хватает краски?: "))

circleArea = pi* d**2 /4
CylArea = pi * d * h
totalArea = circleArea * 2 + CylArea 
totalArea = totalArea*2 if stainIn == "Да" else totalArea

q = totalArea/temp
q = ceil(q)
print("Количество требуемых банок на покраску: ", q)
