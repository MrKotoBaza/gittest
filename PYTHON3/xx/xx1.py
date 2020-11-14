import time
import shutil
import os

sources = list()
target_dir = r"C:\Backups"


while True:
    c = input("Enter path for save or '0': ")
    if c == "0":
        break
    elif os.path.exists(c):
        sources.append(c)
    else:
        print("not exists")

newdir = target_dir+os.sep+time.strftime("%Y%m%d")
if os.path.exists(newdir):
    target = newdir + os.sep + time.strftime("%H%M")
    for i in sources:
        shutil.make_archive(target, "zip", i)
else:
    os.mkdir(newdir)
    target = newdir +os.sep + time.strftime("%H%M")
    for i in sources:
        shutil.make_archive(target, "zip", i)