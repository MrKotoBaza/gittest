print("Same input")
i = int(input())
classes1 = {}
for l in range(0, i):
    line = input()
    line = line.split(":")
    if len(line) == 1:
        line = str(line)
        line = line[2: len(line)-2]
        classes1[line] = []
    else:
        classes1[line[0]] = line[1]
print("What you need?")
q = int(input())
data = []
for n in range(0, q):
    line = input()
    a, b = line.split(":")
    if b in classes1.keys():
        if a in classes1.values():
            data.append("YES")
        else:
            data.append("NO")
    else: 
        data.append("NO")

for s in range(0, q):
    print(data[s])

    


