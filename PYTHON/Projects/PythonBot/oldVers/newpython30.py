fileDB = r"C:\Users\adm\Documents\progpy\file.txt"
def fileWrite(path, data, foundSTR):
    with open (path, 'r') as f:
        old_data = f.read()
        if 'logined' in data: del data['logined']
        new_data = old_data.replace(str(foundSTR), str(data))

    with open (path, 'w') as f:
        f.write(new_data)
foundSTR = ''
data = ["Heelllooo"]
fileWrite(fileDB, data, foundSTR)