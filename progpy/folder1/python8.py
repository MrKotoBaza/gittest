primes=[2, 3, 5]
def isPrime(n):
    container = 0
    for l in primes:
        if n%l != 0:
            container+=1

    if container == len(primes):
        primes.append(n)

for i in range(2, 600851475143):
    isPrime(i)

data = []
primes.reverse()
n = int(input("Enter num: "))
def generateFactors(n):
    for s in primes:
        if n%s ==0:
            data.append(s)
            n = n/s
print(data)
    
#не запускай, убьет
