#converts types to other types

def converteStrToDict(text):
    """
    Interface: 
    text = str() in type dict

    Tries to dict() strings. Else returns False
    """

    try:
        return dict(text)
    except:
        return False
    
def converteStrToList(text):
    """
    Interface: 
    text = str() in type list

    Tries to list() strings. Else returns False
    """

    try:
        return list(text)
    except:
        return False

