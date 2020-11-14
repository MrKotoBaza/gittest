#Сортировка слиянием

def merge(A, B):
    c = [0]*(len(A)+len(B))
    while i<len(a) and k<len(b):
        if A[i] <= B[k]:
            C[n]=A[i]
            i+=1
            n+=1
        else:
            C[n]=B[k]
            k+=1
            n+=1
    C += A
    C += B
    return  C

def merge_sort(A):
    if len(A)<=1:
        return n
    middle = len(A)//2
    L= [A[i] for i in range(0, middle)]
    R= [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = megre(L, R)
    A = list(C)

    