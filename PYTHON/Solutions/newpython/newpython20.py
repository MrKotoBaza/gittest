from math import pi
from math import ceil

print("На какой планете день идет дольше?")
print("Введите данные первой планеты")
name1 = input("Введите имя первой планеты: ")
r1 = float(input("Радиус планеты А: "))
OS1 = float(input("Орбитальная скорость планеты А: "))

print("Введите данные второй планеты")
name2 = input("Введите имя второй планеты: ")
r2 = float(input("Радиус планеты B: "))
OS2 = float(input("Орбитальная скорость планеты B: "))

duration1 = 2*pi*r1*1000000/OS1
duration2 = 2*pi*r2*1000000/OS2

duration1 = duration1/3600/24
duration2 = duration2/3600/24

print("Данные первой планеты: {}".format(name1))
print("Радиус этой планеты (млн. к.): {}".format(r1))
print("Орбитальная скорость этой планеты (км./с.): {}".format(OS1))

print("Данные второй планеты: {}".format(name2))
print("Радиус этой планеты (млн. к.): {}".format(r2))
print("Орбитальная скорость этой планеты (км./с.): {}".format(OS2))

print("Год в днях на планете {0} идет: {1}".format(name1, ceil(duration1)))
print("Год в днях на планете {0} идет: {1}".format(name2, ceil(duration2)))

print("Год в днях идет дольше на планете {}".format(name1 if duration1>duration2 else name2))

