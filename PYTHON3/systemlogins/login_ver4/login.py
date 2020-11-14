import os
import hashlib


class File():
    path: ""
    name: ""
    directory: ""

    def __init__(path):
        if os.path.isfile(path)
        self.path = path
        self.name = os.path.basename(path)
        self.directory = os.path.dirname(path)

    def fileSearch(self, data):
        f = open(self.path, "r")
        count = 0
        output = []
        if type(data) == dict:
            for line in f.readlines():
                line = line[0:-1]
                line = eval(line)
                for key, value in data.items():
                    if value == line[key]:
                        count += 1
                if count == len(data):
                    output.append(True)
                    output.append(line)
                    f.close
                    return output
        f.close()
        output.append(False)
        return output

    def fileWrite(self, data):
        f = open(self.path, "a")
        string = str(data)
        string += "\n"
        f.write(string)
        f.close()
        return True


class User():
    name: ""
    login: ""
    password: ""

    def generateData(self, rangiring):


class System():
    name: ""
    userDataKeys = ['login', 'password', 'name']

    def __init__(name):
        self.name = name

    def instantObjects(self):
        global FileDB = File()
        global User = User()
        global Logs = File()

    def hashing(self, string):
        hash = hashlib.sha256(bytes(string, encoding="utf-8"))
        return hash.hexdigest()
