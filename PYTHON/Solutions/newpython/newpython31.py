#получение значений


print("Вводите числа массива оной строкой с запятыми или без")
print("В конце не должно быть пробела!")
a = ""
while a=="":
    a = input()
a = a.split(", ")
if len(a) == 1:
    a = a[0].split(",")
if len(a) ==1:
    a = a[0].split(" ")
a = list(a)
for d in range(len(a)):
    a[d] = int(a[d])

#перенос данных на другой массив, сохранение

c = []
for x in a:
    c.append(x)

#формирование списка со всеми данными массива

dataMas = [set(a), c]
a.sort()
dataMas.append(a)
dataMas.append(set(a))
l1 = {}
for i in a:
    if i in l1.keys():
        l1[i] +=1
    else:
        l1[i] = 1
dataMas.append(l1)
maxK = 0
maxV = 0
for K, V in dataMas[4].items():
    if V > maxV:
        maxK, maxV = K, V
dataMas.append(maxK)
summ = 0
for i in a:
    summ +=i
dataMas.append(summ)

#output

print("\n \n \n")
s = [x for x in range(len(dataMas)-3)]
print("Вывод данных по ряду чисел")
print(c, "\n")
for l in s:
    print("{} .|\t{}".format(l+1, dataMas[l]), sep = "")
print(l+2," .|", sep = "")
for k, v in dataMas[4].items():
    print("   |\t", k, " - ", v, " times", sep="")
print(l+3, " .|", sep = "")
for k, v in dataMas[4].items():
    print("   |\t", k, " - ", v,"/", len(a), sep = "")
print(l+4, " .|", sep = "")  
for k, v in dataMas[4].items():
    print("   |\t", k, " - ", v/len(a)*100, "%", sep = "")
print(l+5, " .|\t", dataMas[5], sep = "")
print(l+6, " .|\t", summ/len(a), sep="")
if len(a)%2 ==0:
    print(l+7, ".|\t", int((a[int(len(a)/2-1)]+a[int(len(a)/2)])/2), sep ="")
else:
    print(l+7, ".|\t", a[int(len(a)/2)], sep ="")

















