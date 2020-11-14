data = [1, 1]
for i in range(1, 100):
    num = data[i-1]+data[i]
    data.append(num)
    if num/1000000>1:
        print("EEEEE, ",num)
        print(data.index(num))
        break