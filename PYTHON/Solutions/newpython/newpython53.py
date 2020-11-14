list1 = [x for x in range(int(input()), int(input())+1)]
list2 = [y for y in range(int(input()), int(input())+1)]
print(" ", *list2, sep="\t")
for l in range(len(list1)):
    str1 = str(list1[l]) + "\t"
    for i in list2:
        str1+= str(list1[l]*i)+"\t"
    print(str1)