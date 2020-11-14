#Сортировка Тима Хоара (Быстрая сортировка)
def hoar_sort(A):
    if len(A)<=1:
        return
    barrier = A[0]
    L = []
    M=[]
    N=[]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    A = L+M+R
