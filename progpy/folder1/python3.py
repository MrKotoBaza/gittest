primes=[2, 3, 5]
def isPrime(n):
    container = 0
    for l in primes:
        if n%l != 0:
            container+=1

    if container == len(primes):
        primes.append(n)

for i in range(2,600851475143) :
    isPrime(i)
counter = 0
for s in primes:
    counter+= s
print(primes)
print('')
print('')
print('')
print(counter)
#не запускай с этим значением, убьет