def getResult(a):
    a.lower().split(" ")
    c = set(a)
    words = {}
    for i in c:
        words[i] = 0
    for l in c:
        t = a.count(l)
        words[l] = t
    invertedWords = {str(value): key for key, value in words.items()}
    maximal = max(words.values())
    print(invertedWords[str(maximal)], maximal, sep = " ")

def filesget(path):
    fileX = open(path, "r")
    text = ""
    for line in fileX.readlines():
        text = text + line + " "

    getResult(text)

filesget(r"C:\Users\1\Downloads\dataset_3363_3.txt")




