def title():
    print("Программа перевода текста из английской расскладки в русскую.")
    print("Чтобы перевести текст, введите его в следющее место ввода. \nНе забывайте, сообщение должно быть только с английскимим буквами")

def includeVars():
    global convertedTitles
    convertedTitles = {"-":"-"'!':'!', '&':'?', '?':',', "/":".", ' ':' ', 'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю'}
        

def includeString():

    string = input()

    for s in string:
        if s not in "qwertyuiopasdfghjkl;zxcvbnm,.QWERTYUIOPASDFGHJKLZXCVBNM: !&?/-":
            return False
        
    return string

def mainCycle():
    ask = includeString()
    newask = ""
    if ask == False:
        print("Неверное значение, попробуйте еще раз")
        return 

    for i in range(len(ask)):
        if ask[i] in convertedTitles.keys():
                newask += convertedTitles[ask[i]]
        elif ask[i].lower() in convertedTitles.keys():
                    newask+= convertedTitles[ask[i].lower()].upper()

    print(newask)

def main():
    title()
    includeVars()
    while True:
        mainCycle()

main()
    
    

    

    
