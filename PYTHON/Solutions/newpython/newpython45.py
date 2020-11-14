#print("%s %d %2.3f" % ('a', 2, 3.55))
a = int(input())
b = int(input())
c = int(input())

if a >=b and a>=c:
    print(a)
    print(b if b<=c else c)
    print(c if b<=c else b)
elif b>=a and b>=c:
    print(b)
    print(a if a<=c else c)
    print(c if a<=c else a)
else:
    print(c)
    print(a if a<=b else b)
    print(b if a<=b else a)