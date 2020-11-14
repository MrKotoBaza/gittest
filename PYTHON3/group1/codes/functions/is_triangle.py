print("Is it triangle?")
print("Get all 3 sides of triangle")
a = float(input("Input first side of triangle 15"))
b = float(input("Input second side of triangle "))
c = float(input("Input third side of triangle "))
if a+b > c and b+c > a and a+c > a:
    if a==b and b==c:
        print("It is a equilateral triangle")
    elif a==b or b==c or a==c:
        print("It is a isosceles triangle")
    else:
        print("It is a triangle")
else:
    print("It isn't triangle")

