import math
userNumber = int(input("n: "))
numberOfPrimes = 0

for x in range(userNumber):
    currentNumber = 1
    numberOfDivisions = 0
    while (currentNumber<x)&(numberOfDivisions<2):
        if x%currentNumber==0:
            numberOfDivisions += 1
        currentNumber += 1
    if numberOfDivisions==1:
        numberOfPrimes += 1
print("Number of primes: " + str(numberOfPrimes))