thisNumber = 2
lastNumber = 1
fibsum = 0

while thisNumber < 4000000:
    if thisNumber%2==0:
        fibsum += thisNumber

    nextNumber = thisNumber + lastNumber
    lastNumber = thisNumber
    thisNumber = nextNumber

print(fibsum) #4613732
