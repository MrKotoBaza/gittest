import string, random

using = string.digits + string.ascii_letters
    
print(using)
string = "".join([random.choice(using) for i in range(10)])

print(string)