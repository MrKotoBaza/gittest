def checkLogin(data:dict, c:int):
    """
    Interface:
        data = dict()
    
    In DATA: login, password
    Returns True if data is in file path
    Returns False if not
    """
    ansv = fileSearchDicts(FULLPATH, data, c)
    if ansv == False:
        return False

    else:
        return ansv

def checkReg(data:dict, c:int):
    """
    Interface:
        data = dict()
    Returns True if user registred in system Else false
    Returns False if user is in file database or other Error
    """
    ansv = fw.fileSearchDicts(FULLPATH, data, c)
    if ansv == False:
        fw.fileWrite(FULLPATH, data)
        return data

    else:
        return False

def login(login:str, passw:str):
    """
    Interface:
        login = str()
        passw = str()
    """
    d = {'login': login, 'passw': passw}
    count = 2
    ansv = checLogin(d, count)
    if ansv == False:
        raise ValueError
    else:
        return ansv

def regin(login:str, passw:str)


