string = input()

c = string[0]
num = 1

str1 = ""
for x in range(1, len(string)):
    if x <len(string) and string[x-1] != string[x]:
        str1+= c + str(num)
        c = string[x]
        num = 1
    else:
        num+=1
str1 += c + str(num)
print(str1)
        