def get_primes(n):
    primes = [2, ]
    i = 3
    while primes[-1] < n:
        print "Passage pour i = " + str(i)
        print "Nombre de nombres premiers: " + str(len(primes))
        for p in primes:
            if i% p == 0:
                break
            if p == primes[-1]:
                primes.append(i)
        i += 1
    primes.pop()

    return primes

if __name__ == "__main__":
    n = 2000000
    primes = get_primes(n)
    sum = 0

    for p in primes:
        sum += p

    print sum

