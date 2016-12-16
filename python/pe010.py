def listPrimesUnderN(n):
    primes = list([2])
    counter = 3

    while primes[-1] < n:
        # Printing at a reasonable rate so you know it's still running
        if len(primes)%100==0:
            print("N Primes:\t{}\nMax Prime:\t{}".format(len(primes),primes[-1]))
        isPrime = True

        for p in primes:
            if counter%p == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(counter)

        # Incrememnt by 2 to avoid even numbers
        counter += 2

    primes.pop()

    return primes

if __name__ == '__main__':
    n = 2000000
    primes = listPrimesUnderN(n)

    sumprimes = sum(primes)
    print(sumprimes) #142913828922
