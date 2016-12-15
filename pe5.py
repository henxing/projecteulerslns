from pe3 import listPrimeFactors

def nSmallestMultiples(n):
    multipliers = list()
    for i in range(n,0,-1):
        pf = listPrimeFactors(i)

        to_add = list()
        these_multipliers = list(multipliers)
        for factor in pf:
            isIncluded = False

            for m in these_multipliers:
                if factor == m:
                    these_multipliers.remove(m)
                    isIncluded = True
                    break

            if not isIncluded:
                multipliers.append(factor)

    return multipliers

if __name__=="__main__":
    n = 20
    sm = nSmallestMultiples(n)
    smallest_multiple = 1
    for m in sm:
        smallest_multiple *= m

    print(smallest_multiple) #232792560
