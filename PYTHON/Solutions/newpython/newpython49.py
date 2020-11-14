def f(l):
    lst1 = []
    for i in range(len(l)):
        if l[i] %2 == 0:
            l[i] = l[i]//2
        else:
            lst1.append(i)
    lst1.reverse()
    for s in lst1:
        del l[s]

lst = [0, 0, 0]
f(lst)
print(lst)
