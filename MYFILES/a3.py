with open(r"C:\Users\Aiskuriimu\Downloads\26_demo.txt", "r") as f:
    s = f.readline().split()
    mass = []
    for i in f.readlines():
        mass.append(int(i))

    mass.sort()
    sum_f = []
    for i in range(int(s[1])):
        if sum(sum_f) + mass[i] <int(s[0]):
            sum_f.append(mass[i])
        elif  



        