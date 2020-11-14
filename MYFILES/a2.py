w = 5
h = 5
mass = [[0]*w for i in range(h)]
quadrats = [
    '1 1 3 3',
    '2 2 4 4'
]
def aggregate(mass, what):
    for o in what:
         cords = o.split()
         cords = list(map(int, cords))
         print(cords)
         for i in range(cords[0], cords[2]):
             for j in range(cords[1], cords[3]):
                 mass[i][j] = 1

aggregate(mass, quadrats)

summ = 0
for i in mass:
    for j in i:
        if j == 0:
            summ += 1


print(summ)
print("\n\n\n\n")
for i in mass:
    print(*i, sep = ' ')