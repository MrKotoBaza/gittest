def find():
    c = [i**2 for i in range(1, 101)]
    s = sum(range(1, 101)) ** 2

    print(s - sum(c))
