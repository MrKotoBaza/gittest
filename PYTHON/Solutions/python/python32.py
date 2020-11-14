def gen_numbers(N, M, prefix=None):
    """Задача генерации последовательности из M чисел в системе счисления N"""
    if M==0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        gen_numbers(M, M-1, prefix)
        prefix.pop()

def gen_permutations(N, M, prefix=None):
    """Задача генерации последовательности из M чисел в системе счисления N без повторение чисел"""
    if M==-1:
        M=N
    prefix = prefix or []
    if M==0:
        print(prefix)
        return
    for digit in range(1, N+1):
        if digit in prefix:
            continue
        prefix.append(digit)
        gen_numbers(M, M-1, prefix)
        prefix.pop()

gen_numbers(3, 3)
print("||||||")
gen_permutations(3, 3)