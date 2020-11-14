"""Bubble Sort"""

def buble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    

list1 = [1, 5, 7, 6, 5, 4, 3, 7, 8]
buble_sort(list1)
print(list1)