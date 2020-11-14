print("Вывод уравнения прямой на основе двух её точек")
print("Введите значение координат точки А")
x1 = float(input("\tx: "))
y1 = float(input("\ty: "))
print("Введите значение координат точки B")
x2 = float(input("\tx: "))
y2 = float(input("\ty: "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2

print("Результат: y = %.2f*x + %.2f" % (k, b))