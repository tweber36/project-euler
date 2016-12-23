def get_primes(n):
    primes = [2, ]
    i = 3
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
            if p == primes[-1]:
                primes.append(i)
        i += 1

    return primes

if __name__ == "__main__":
    res = get_primes(10001)
    print res[-1]


