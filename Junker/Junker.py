import os
import random

# r=root, d=directories, f = files
def randstring(length):
    words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''
    for i in range(0, length):
        string = string + words[random.randint(0, 23)]
    return string
    
def getallsubdirs(dir):
    folders = [dir]
    for r, d, f in os.walk(dir):
        for folder in d:
            folders.append(os.path.join(r, folder))

    return folders

def Junker(msg, n):
    subdirs = getallsubdirs('.')
    for x in range (0, len(subdirs)):
        for i in range (0, n):
            random.randint
            f = open(subdirs[x] + '/' + randstring(8) + '.txt', 'w')
            f.write(msg)
            f.close
        x = x + 1


def takeinput():
    try:
        msg = input('Enter message: ')
        n = int(input('Enter number of files to create in each subdir: '))
    except:
        takeinput()
    Junker(msg, n)

takeinput()
