primes=[2, 3, 5]
def isPrime(n):
    container = 0
    for l in primes:
        if n%l != 0:
            container+=1

    if container == len(primes):
        primes.append(n)
def main(data):
    """Ищет простые числа в наборе
    Interface:
    data = int
    """
    for i in range(2,data) :
        isPrime(i)
    counter = 0
    for s in primes:
        counter+= s
    print(primes, "\n\n\n", counter)
data = int(input("Enter num: "))
main(data)
#не запускай с этим значением, убьет