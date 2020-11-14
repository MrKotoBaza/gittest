def fibonacci(a, b):
    if b >1000:
        return "stop"
    else:
        c = a+b
        print(c)
        return fibonacci(b, c)
fibonacci(1, 1)

    





