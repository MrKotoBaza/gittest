import hashlib
import uuid

def hashData(text1):
    """
    Interface:
        text1 = str()
    Returns hashed text with salt
    """
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text1.encode()).hexdigest() + ':' + salt

def reHashData(text1, text2):
    """
    Interface: 
        text1 = str()
        text2 = str()
    Returns True if text1 == text2 else False
    """
    hashedText, salt = text2.split(':')
    return hashedText == hashlib.sha256(salt.encode() + text1.encode()).hexdigest()