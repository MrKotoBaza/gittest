from random import randint
arr = [randint(1, 9) for x in range(1000000)]

count_1_3 = 0
count_4_6 = 0
count_7_9 = 0

for i in arr:
    if 1<=i<=3:
        count_1_3 +=1
    elif 4<=i<=6:
        count_4_6+=1
    elif i<=7<=9:
        count_7_9+=1
print(count_1_3)
print(count_4_6)
print(count_7_9)
print(count_1_3+count_4_6+count_7_9)

