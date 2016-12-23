def get_primes(n):
    primes = [2,]
    for i in range(2,n):
        for p in primes:
            if i % p == 0:
                break
            if p == primes[-1]:
                primes.append(i)
    return primes

def divisible_by_all(n):
    primes_list = get_primes(n)
    
    res = 1
    min_factors = {}

    for p in primes_list:
        min_factors[p] = 1
    
    for i in range(2,n):
        factors = {}
        for p in primes_list:
            if p > i:
                break
            factors[p] = 0
            while i % p == 0:
                factors[p] += 1
                i = i/p
        for x, y in min_factors.items():
            if x in factors.keys() and factors[x] > y :
                min_factors[x] = factors[x]

    for x, y in min_factors.items():
        res *= pow(x, y)
    
    return res



if __name__ == "__main__":
    print(divisible_by_all(1000))
