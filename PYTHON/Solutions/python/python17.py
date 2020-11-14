import hashlib
import uuid

fileDB = r"C:\Users\adm\Documents\progpy\file.txt"
userdata={'login':'root', 'password':'root', 'userLevel':'Infinity', 'isAdmin': 'True', 'type': 'user'}
def dataRedo(data):
    reData = {}
    reData['login'] = data['login']
    reData['password'] = data['password']
    return reData

def fileWrite(path, data):
    with open (path, 'r') as f:
        old_data = f.read()
        dataRe = dataRedo(data)
        foundSTR = fileLogin(path, dataRe)[1]
        new_data = old_data.replace(str(foundSTR), str(data))
    with open (path, 'w') as f:
        f.write(new_data)

def hashData(text1):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text1.encode()).hexdigest() + ':' + salt

def reHashData(text1, text2):
    password, salt = text2.split(':')
    return password == hashlib.sha256(salt.encode() + text1.encode()).hexdigest()

def fileLogin(path, data):
    #импорт data в приведенном виде
    f = open(path, "r")
    count = 0
    result = []
    for line in f.readlines():
        line = eval(line)
        for key, value in data.items():
            if value != line[key]:
                count += 1
        if count == 0:
            result.append(True)
            result.append(line)
            return result
    f.close()
    result.append(False)
    return result


fileWrite(fileDB, userdata)