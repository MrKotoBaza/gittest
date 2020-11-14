def deposite(a, year):
    sum = a
    while year>0:
        sum += a*(0.1)
        year-=1
    return sum
print(deposite(5000, 10))
