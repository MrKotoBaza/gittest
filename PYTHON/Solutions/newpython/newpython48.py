a = int(input())
b = int(input())
c = a 
f = b 
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
d = a+b
print(int(c*f/d))
 
