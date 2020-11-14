from faceCamera import faceDetection #Распознавание лица в реальном времени
from facePhoto import faceDetection as facePhoto #Распознавание лица на фотографии
import tkinter as tk
from tkinter import filedialog as fg

def main():
    """
    Создание окна для всей программы
    """
    root = tk.Tk()
    root.title("Обнаружение лиц")
    root.geometry("")
    fr = tk.Frame(root)
    lbl1 = tk.Label(fr, text="Программа по обнаружению лиц", font = ['Arial', 10])
    lbl2 = tk.Label(fr, text="Чтобы запустить обнаружение лиц, нажмите на одну из двух кнопок ниже", 
                    font=["Arial", 10])
    lbl3 = tk.Label(fr, font=["Arial", 10], text="Кнопка <Камера> создаст обнаружение лица в реальном времени")
    lbl4 = tk.Label(fr, font=["Arial", 10], text="Кнопка <Загрузить фотографию> создаст обнаружение лица на изображении")
    btn1 = tk.Button(root, text="Камера", command = faceDetection)
    btn3 = tk.Button(root, text="Загрузить фотографию", command = getFileForPhoto)
    btn4 = tk.Button(root, text="Закрыть", command = close)

    lbl1.grid(row = 0, column = 0, columnspan = 3, sticky = "nw")
    lbl2.grid(row = 1, column = 0, columnspan = 3, sticky = "nw")
    lbl3.grid(row = 2, column = 0, columnspan = 3, sticky = "nw")
    lbl4.grid(row = 3, column = 0, columnspan = 3, sticky = "nw")
    fr.grid(row = 0, column = 0, columnspan = 3, sticky = "nw", pady = 15)
    btn1.grid(row = 4, column = 0, sticky = "sw", padx = 10)
    btn3.grid(row = 4, column = 2, sticky = "sw", padx = 10)
    btn4.grid(row = 4, column = 3, sticky = "sw", padx = 10)
    root.mainloop()

def close():
    """
    Закрытие программы
    """
    exit()

def getFileForPhoto():
    """
    Функция ищет изображение и передает путь к нему функции распознавания лиц на фотографии 
    """
    path = fg.askopenfilename(filetypes=[('All files','*.*'),
                                        ('PNG pictures','*.png'),
                                        ('JPEG pictures','*.jpg')])
    print(path)
    try:
        facePhoto(path)
    except:
        pass

main()