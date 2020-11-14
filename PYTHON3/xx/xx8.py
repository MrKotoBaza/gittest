
cashe = {}

def fibonacci(n):
    global cashe

    if n in cashe:
        return cashe[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
    cashe[n] = result
    return result

for i in range(20, 1000):
    print(i, fibonacci(i))

