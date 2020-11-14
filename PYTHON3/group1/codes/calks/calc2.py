def arithmetic(n1, n2, op):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2
    else:
        return("Unknown operation")
num1 = int(input("Get first num "))
num2 = int(input("Get second num "))
operate = input("Get operation ")
print(arithmetic(num1, num2, operate))