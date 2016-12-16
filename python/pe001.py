def sumMultiples(max_value):
    thesum = 0

    for i in range(max_value):
        if i%3==0 or i%5==0:
            thesum += i

    return thesum

if __name__=="__main__":
    max_value = 1000
    thesum = sumMultiples(max_value)
    print(thesum) # 233168
