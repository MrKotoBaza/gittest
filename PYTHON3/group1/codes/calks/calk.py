print("Это калькулятор на Python")
print("Чтобы завершить работу, введите ответ на первый вопрос 'stop'")
while True:
    operation = input("Какую операцию вы хотите провести с числами? (дано +, -, *, /, ^, stop): ")
    if operation == "stop":
        break
    elif operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "^" :
        print("Error: Undefined operation. Please, input only '+', '-', '*', '/', '^'")
    else:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if operation == "+":
            print(num1+num2)
        elif operation == "-":
            print(num1-num2)
        elif operation == "*":
            print(num1*num2)
        elif operation == "/":
            print(num1/num2)
        else:
            print(num1**num2)
