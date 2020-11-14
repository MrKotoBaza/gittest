def converteStrings(data):
    string = data
    str1 =""
    dict1 = {}
    for x in range(len(string)-1):
        if string[x].isalpha():
            c = string[x]
            dict1[c] = ''
            i = x+1
            while i<len(string) and string[i].isdigit():
                dict1[c] += string[i]
                i+=1
            dict1[c] = int(dict1[c])
    for key, val in dict1.items():
        str1+= key*val 
    print(str1)         
    return str1
#WORKS
with open(r"dataset_3363_2.txt", 'r') as inp, open(r'ret.txt', 'w') as out:
    out.write(converteStrings(inp.read()))
