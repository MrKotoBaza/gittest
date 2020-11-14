import os
def fileWrite(path, text):
    """
    Inteface:
    path - path to file
    text = str()

    Writes text to a file by adding
    """
    with open(path, 'r') as f:
        old_data = f.read()
        new_data = old_data+text

    with open (path, 'w') as f:
        f.write(new_data)

def fileRead(path, text):
    """
    Interface:
    path - path to file
    text = str()

    Returns True if in file with path there is a text
    """

    with open(path, "r") as f:
        data = f.read()

        if text in data:
            return True
        else:
            return False

def fileReadDicts(path, data:dict):
    """
    Interface:
    path - path to file
    data = dict()

    Returns full dict if in file with path there is a dict==data
    """
    with open(path, "r") as f:
        for line in f.readlines():
            line = eval(line)
            count = 0

            for key, val in data.items():
                if val != line[key]:
                    count+=1
            if count == 0:
                break
        else: 
            return False

        return line

def fileReadLists(path, data:list):
    """
    Interface:
    path - path to file
    data = list()

    Returns full list if in file with path there is a list==data
    """
    with open(path, "r") as f:
        for line in f.readlines():
            line = eval(line)
            count = 0

            if len(line)== len(data):
                for i in range(len(data)-1):
                    if data[i]!=line[i]:
                        count+=1
            if count == 0:
                break
        else: 
            return False
        return line

def fileSearchDicts(path, data:dict c:int):
    """
    Interface:
        path = path to file
        data = dict()
        c = count of needs overlap

        Returns full dict if data in path to file has c coincidences
        Else returns False
    """
    pass
