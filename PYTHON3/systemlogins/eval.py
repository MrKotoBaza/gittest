file = "string+"
def stringexpand():
    inp = input("Enter new string")
    global file
    file= file + inp
print(file)
stringexpand()
print(file)
# global заставляет переменную связаться с глобальной такой же переменной. Обычно переменные объявляются локальными и никак не взяимодействуют с глобальным окружением (return)
