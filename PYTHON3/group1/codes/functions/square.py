from math import sqrt
def square(a):
    p = a*4
    s = a*a
    d = sqrt(a**2 + a**2)
    mas = str(p) + " " + str(s) + " " + str(d) + " "
    return mas
i = int(input("Get a number"))
print(square(i))