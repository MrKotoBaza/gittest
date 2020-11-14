c = [0, 1]
s = int(input())
i = 1
while c[i] < s:
    i+=1
    c.append(c[i-1]+c[i-2])
if c[-1] == s:
    print(len(c)-1)
else:
    print(-1)
