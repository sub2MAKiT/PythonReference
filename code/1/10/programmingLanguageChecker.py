from dataclasses import dataclass

def recursive(x):
    if isfile(x):
        fileArray.append(x)
    else:
        tempArr = listdir(x)
        for a in tempArr:
            recursive(x+'/'+a)

@dataclass
class file:
    E: list
    N: list
    V: list
    S: int

from os import listdir
from os.path import isfile, join
pathArray = ['.','/','c','h','e','k']
fileArray = []
fileE = file([],[],[],0)
with open('./languagesList.MKTI') as f:
    contents = f.read()
    for x in range(len(contents)):
        if (contents[x-1]=='\n')|(x==0):
            fileE.E.append([])
            fileE.N.append([])
            fileE.V.append(0)
            offset = 0
            while contents[x+offset]!='-':
                fileE.E[fileE.S].append(contents[x+offset])
                offset += 1
            offset +=1
            while (contents[x+offset]!='\n')&(x+offset+1<len(contents)):
                fileE.N[fileE.S].append(contents[x+offset])
                offset+=1
            fileE.S +=1
for x in listdir(''.join(pathArray)):
    recursive(''.join(pathArray)+'/'+x)
for x in fileArray:
    with open(x) as f:
        contents = f.read()
        dotPlace = 0
        for a in range(len(x)):
            if x[len(x)-a-1] == '.':
                dotPlace = len(x)-a
                break
        fileExtension = []
        for a in range(len(x)-dotPlace):
            fileExtension.append(x[a+dotPlace])
        for a in range(len(fileE.E)):
            if len(fileExtension)==len(fileE.E[a]):
                for b in range(len(fileE.E[a])):
                    cheese = 0
                    if fileE.E[a][b] != fileExtension[b]:
                        cheese = 1
                    if cheese == 0:
                        fileE.V[a] += len(contents)
                    break
for x in range(len(fileE.E)):
    print('{}: {}'.format(''.join(fileE.N[x]),str(fileE.V[x])))