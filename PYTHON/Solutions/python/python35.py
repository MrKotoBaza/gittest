#Проверка отсортированности массива

def check_sorted(A, asc=True):
    flag = True
    s = 2*(int(asc))-1
    for i in range(0, len(A)-1):
        if s*A[i]>S*B[i]:
            flag = False
            break
    return flag

