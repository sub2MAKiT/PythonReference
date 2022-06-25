import time
import os
sizeOfClock = int(input("size of counter: "))
counter = 0
offset = 0 # I'm not happy about this approach either, but I have no idea how to do it in python

while 1:
    if len(str(counter)) > sizeOfClock:
        offset = len(str(counter)) - sizeOfClock
    print("+",end='')
    for x in range(sizeOfClock+offset):
        print("-",end='')
    print("+")
    print("|",end='')
    for x in range(sizeOfClock-len(str(counter))): # len(str(counter))>sizeOfClock?len(str(counter))-sizeOfClock:0
        print("0",end='')
    print(str(counter),end='')
    print("|")
    print("+",end='')
    for x in range(sizeOfClock+offset):
        print("-",end='')
    print("+")
    time.sleep(1)
    counter = counter + 1
    os.system('cls')