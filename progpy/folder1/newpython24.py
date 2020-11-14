for i in range(2, 300000):
    print(i)
    while i != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = (i*3 +1)/2
    print("Ready")
#не запускай, убьет