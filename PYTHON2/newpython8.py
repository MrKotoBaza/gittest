def lcs(a, b):
    F - [[0]*(len(b)+1) for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                f[i][j] = 1+ =[i-1][j-1]
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])

    return f[-1][-1]

    #i don't know how it work
    # ;( 
    # что таке подпоследовательность????      

def gis(a):
    F = [0]*len(a)+1
    for i in range(1, len(a)+1):
        m = 0
        for j in range(0, i):
            if a[i] > a[j] and F[j]>m:
                m = F[j]

        F[i] = m+1
    return F[-1]

def levenstein(A, B):
    F = [[ (i+j) if i*j == 0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1+min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[-1][-1]

def equal(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True



def searchSubStringLINGHT(s, sub):
    for i in range(len(s)-len(sub)):
        if equal(s[i:i+len(sub)], sub):
            print(i)














