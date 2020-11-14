def levenstein(a, b):
    f = [[i+j if i*j == 0 else 0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1 ,len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1+ min(f[i][j-1], f[i-1][j])

    return f[len(a)][len(b)]

def prefix(s):
    P = [0 for i in range(len(s))]
    for i in s:
        p = P[i-1]
        while p >0 and s[i] != s[p+1]:
            p = P[p]
        if s[i] == s[p+1]:
            p += 1
        P[i] = p

def kmp(s, sub):
    sx =  sub + "#" + s
    #use prefix_function

#stack / очередь LIFO kast in first out

#если использовать в докстроках синтаксс интерпретатора пайтона, а потом использовать doctest.testmode(), произведется тест программы на основе докстроки
#doctest.testmode(verbose = True) - опция "громкого" тестирования

_stack = []

def push(x):
    _stack.append(x)

def pop():
    return _stack.pop()

def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0







