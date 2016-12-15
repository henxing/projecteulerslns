def listNprimes(n):
    primes = list([2])
    counter = primes[0]

    while len(primes) < n:
        isPrime = True

        for p in primes:
            if counter%p == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(counter)

        counter += 1

    return primes

if __name__=="__main__":
    n = 10001
    primes = listNprimes(n)
    print(primes[-1]) #???
