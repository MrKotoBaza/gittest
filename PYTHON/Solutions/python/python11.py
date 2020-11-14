#test

path = r"C:\Users\adm\Documents\progpy\path.txt"
def fileReadTF(path, data):
    file = open(path, "r")
    count = 0
    for line in file.readlines():
        line = eval(line)
        for key, value in data.items():
            if value != line[key]:
                count += 1
        if count == 0:
            return True
    file.close()
    return False
print(fileReadTF(path, {'login':'hello', 'password':'world'}))