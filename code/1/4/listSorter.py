def readCurrentLineNumber(content,charNumber):
    endSize = 0
    tempArray = [content[charNumber]]
    while (ord(content[charNumber+endSize+1])>47)&(ord(content[charNumber+endSize+1])<58):
        endSize += 1
        tempArray.append(content[charNumber+endSize])
    return int(''.join(tempArray))

def readCurrentString(content,charNumber):
    endSize = 0
    tempSize = 0
    while content[charNumber+endSize-1]!='.':
        endSize += 1
    while (content[charNumber+endSize+tempSize]!='\n')&(charNumber+endSize+tempSize+1<len(content)):
        tempSize += 1
    tempArray = [content[charNumber+endSize]]
    for x in range(tempSize-1):
        tempArray.append(content[charNumber+endSize+tempSize])
    return ''.join(tempArray)
        

with open('./list.MKTI') as f:
    contents = f.read()
    x = ["test"]
    for a in contents:
        if a=='\n':
            x.append("test")
    for a in range(len(contents)):
        if (contents[a-1]=='\n')|(a==0):
            x[readCurrentLineNumber(contents,a)-1] = readCurrentString(contents,a)
    for a in x:
        print(a,end='')

