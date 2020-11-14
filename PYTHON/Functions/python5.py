def counting(n):
    counter = 0
    while n != 1:
        if n%2 ==0:
            n/=2
        else:
            n=3*n+1
        counter +=1
    return counter
def main(num):
    """
        не запускай, убьет
        Interface:
        num = int
    """
    source = []
    for s in range(1, num):
       source.append(counting(s))

    print(max(source))
num = int(input("Enter num: "))
main(num)