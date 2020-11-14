M = 8
N = 8
mass = [[0]*M for i in range(N)]

for k in range(M):
    mass[0][k] = 0
    mass[1][k] = 1

for c in range(N):
    mass[c][0] = 0
    mass[c][1] = 1

mass[1][1] = 2
    


for i in range(N):
    for j in range(M):
        mass[i][j] = mass[i-1][j] + mass[i][j-1]

#for d in range(N):
#    print(*mass[d], sep = " ")

print(mass[N-1][M-1])




