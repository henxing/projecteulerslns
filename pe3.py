def projecteuler003(n):
    i = 2
    prime_factors = list()
    while i ** 2 <= n:
        if n%i==0:
            prime_factors.append(i)
            n /= i
        else:
            i += 1

    prime_factors.append(n)
    return prime_factors

if __name__=="__main__":
    n = 600851475143
    prime_factors = projecteuler003(n)
    print(prime_factors[-1]) #6857
