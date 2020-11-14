from math import sqrt

a = sqrt(425)
b = sqrt(394)
c = 14
p = (a+b+c)/2
print(sqrt(p*(p-a)*(p-b)*(p-c)))