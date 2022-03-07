import os
import linecache

with open('temp.tmp') as f:
    tempdata = f.read()

with open('wallpath.txt', "w") as f:
    for line in tempdata:
        line = line.replace(' ', '')
    f.write(tempdata)
    f.close()
print(line)
os.remove('temp.tmp')

# extracting the 5th line
wallpath = linecache.getline('wallpath.txt', 3)
wallpath = wallpath.replace('WallPaper    : ', '')
rest = linecache.getline('wallpath.txt', 4)
if "PSPath       :" not in rest:
    wallpath = wallpath + rest.replace(' ', '')
    wallpath = wallpath.replace('\n', '')
with open('wallpath.txt','r') as f:
    replace = ""
    for line in tempdata:
        line = line.replace(' ', '')
    f.close()

    # opening the file in write mode
    with open('wallpath.txt', "w") as f:
        f.write(wallpath)
        f.close()
    #f.write()

print(wallpath)

quit()