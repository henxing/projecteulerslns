from operator import mul

def pythagoreanSum(n):
    for a in range(1, n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                if (a**2 + b**2 == c**2) and (a + b + c == n):
                    return (a, b, c)

if __name__ == '__main__':
    n = 1000
    triple = pythagoreanSum(n)
    product = reduce(mul, triple, 1)
    print(product) #31875000
