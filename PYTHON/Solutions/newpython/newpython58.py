def filling(path):
    fileDB = open(path, "r", encoding="utf-8")
    for line in fileDB.readlines():
        classes[str(int(line[0:2]))].append(line[-4:-1])
    fileDB.close()

classes = {}

for i in range(11):
    classes[str(i+1)] = []

filling(r"C:\Users\1\Downloads\dataset_3380_5.txt")

for x in classes.keys():
    s = 0
    count = 0
    if classes[x]:
        for k in classes[x]:
            s+= int(k)
            count+=1
        classes[x] = s/count
    else:
        classes[x] = "-"

for a, b in classes.items():
    print(a, b, sep=" ")






    
    
