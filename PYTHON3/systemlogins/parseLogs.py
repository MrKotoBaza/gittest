def parseLog(filePath, searchEl):
    f = open(filePath, 'r')
    fileData = []
    count = 0
    for line in f.readlines():
        fileData.append(line)
    for line in fileData:
            line = eval(line)
            if searchEl in line:
                print(line)
                count+=1
    if count ==0:
            print("not found")
while True:
    print("Logs parsing")
    print("You can search by login, name, action and result")
    inp = input("Enter, what string in logs you need: ")

    parseLog(r"C:\Users\Александра\Desktop\progpy\login_ver2\logs.txt", inp)
    #вывод только каких-то звчений по условию 
    #поиск по времени
    #
    # 
    #