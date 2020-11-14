l = []
c = int(input())
i = 1
while True:
    a = int(input())
    if a ==0:
        l.append(i)
        break
    else:
        if a ==c:
            i+=1
        else:
            c = a
            l.append(i)
            i = 1
print(max(l))

 