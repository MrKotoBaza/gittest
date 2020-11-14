primes=[2, 3, 5]
def isPrime(n):
    container = 0
    for l in primes:
        if n%l != 0:
            container+=1

    if container == len(primes):
        primes.append(n)

for i in range(2, 100000):
    isPrime(i)

print(primes)
    
#не запускай, убьет
