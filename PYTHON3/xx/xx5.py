def capitaliz(string):
    string2 = []
    string = string.split(" ")
    for i in string:
        i = i.capitalize()
        string2.append(i)
        

    return " ".join(string2)    


print(capitaliz("you need remove"))