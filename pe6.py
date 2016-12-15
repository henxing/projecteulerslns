def squareSumMinusSumSquare(n):
    squareSum = 0
    sumSquare = 0

    for i in range(n+1):
        squareSum += i
        sumSquare += i**2

    squareSum *= squareSum
    return squareSum - sumSquare

if __name__=="__main__":
    n = 100
    ssmss = squareSumMinusSumSquare(n)
    print(ssmss) #25164150
