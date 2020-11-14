def shift(arr, steps):
    for i in range(steps):
        print(i)
        l = arr[len(arr)-1]
        arr.pop(len(arr)-1)
#задача о циклическом сдвиге