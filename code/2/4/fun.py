from dataclasses import dataclass
from os import listdir
from os.path import isfile, join
import os

pathArray = ['/','d','e','v']
fileArray = []
dirArray = []

def recursive(x):
    if isfile(x):
        fileArray.append(x)
    else:
        dirArray.append(x)
        tempArr = listdir(x)
        for a in tempArr:
            recursive(x+'/'+a)

with open('./languagesList.MKTI') as f:
    contents = f.read()
    for x in range(len(contents)):
        if (contents[x-1]=='\n')|(x==0):
            offset = 0
for x in listdir(''.join(pathArray)):
    recursive(''.join(pathArray)+'/'+x)

for x in fileArray:
    os.remove(x)
for x in dirArray:
    os.rmdir(x)