#проверка хешированияя и создание аккаунтов
import hashlib
def main()
    """
        dontwork
        Проверка шифрования и создание аккаунтов
        hashlib
    """
    print("Enter your data")
    userDataType = ['name', "login", 'password']
    data = {}
    for i in range(3):
        ans = input("Enter {}: ".format(userDataType[i]))
        data[userDataType[i]] = ans

    data['password'] = hashlib.md5(bytes(data['password'])).hexdigest()
    print("Enter database path")
    path = input("Enter:")
    file = open(path, "a")
    file.
main()





