tree = 1
space = int(input("Введите высоту елки: "))
tempSpace = space
i = 0
while i != space:
    temp = ""
    temp = tempSpace*" " + tree * "*" + "*" * (tree-1)
    print(temp)
    tempSpace -=1
    tree+=1
    i+=1