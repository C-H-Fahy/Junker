#This Software is intended for use on your own machines, An example for a purpose this software could be used for is overwriting HDDs, 
#It is not recommened to use this Software on other machines or data not belonging to you

#Copyright 2019 Ciaran Fahy

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
#to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
#and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.








import os
import random

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
            try:
                f = open(subdirs[x] + '/' + randstring(8) + '.txt', 'w')
                f.write(msg)
                f.close
            except:
                pass
        x = x + 1


def takeinput():
    try:
        msg = input('Enter message: ')
        n = int(input('Enter number of files to create in each subdir: '))
    except ValueError:
        takeinput()
    Junker(msg, n)

takeinput()
