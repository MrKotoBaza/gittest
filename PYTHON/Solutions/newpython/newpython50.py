str1 = input()
list1 = str1.split(" ")
x = input()
pos = ''
if x not in list1:
    print("Отсутствует")
elif x == list1[0] and len(list1)==1:
    print(0)
else:
    for i in range(len(list1)):
        if list1[i] == x:
            pos+= str(i)+ " "
print(pos)
