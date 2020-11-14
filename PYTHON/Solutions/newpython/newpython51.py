str1 = input().lower().split(" ")
d = {}
for x in str1:
    d[x] = d[x]+1 if x in d.keys() else 1
for x in d.keys():
    print(x, d[x])

