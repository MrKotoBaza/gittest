a=[]
for i in range(0,120):
    a.append(0)
file=open(r"C:\Users\Aiskuriimu\Desktop\GITHUBTEST\onthisdevice\allcode\28133_A.txt","r")
file.readline()
n1=0
n2=0
for line in file:
    t=int(line)%120
    if t==0:
        t=120
    if a[120-t] > int(line) and a[120-t]+int(line) > n1+n2:
        n1=a[120-t]
        n2=int(line)
    if t<120:
        if a[t]<int(line):
            a[t]=int(line)
    elif int(line)>a[0]:
        a[0]=int(line)

if n1+n2!=0:
    print(n1,n2)
else:
    print("00")