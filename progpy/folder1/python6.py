source = []
for i in range(1, 100000):
    if i%3 ==0 or i%5 == 0:
        source.append(i)
counter = 0
for s in source:
    counter+=s

print(counter)