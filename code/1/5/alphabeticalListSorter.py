with open('./list.MKTI') as f:
    contents = f.read()
    finalArray = []
    for a in range(len(contents)):
        if (contents[a-1]=='\n')|(a==0):
            tempSize = 0
            tempArray = [contents[a]]
            while (tempSize+1+a!=len(contents))&(contents[a+tempSize]!='\n'):
                tempSize +=1
                tempArray.append(contents[a+tempSize])
            finalArray.append(''.join(tempArray))       
finalArray.sort()
for x in finalArray:
    print(x,end='')

