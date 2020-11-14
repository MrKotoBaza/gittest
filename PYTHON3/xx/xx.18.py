c = [i for i in range(999, 500, -1)]
n = []
for i in c:
    for j in c:
        d = str(j*i)
        if d[:3] == d[:-4:-1]:
            n.append(d)
print(max(n))
            
        
                   
