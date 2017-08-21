def is_prime(n):
    if n < 0:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


def number_of_primes(a, b):
    n = 0
    while is_prime(n*n + a*n + b):
        n += 1
    return n

if __name__ == '__main__':
    max_number_primes = 0
    product = 0
    for i in range(-1000, 1001):
        for j in [x for x in range(2, 1001) if is_prime(x)]:
            nb_primes = number_of_primes(i, j)
            if nb_primes > max_number_primes:
                max_number_primes = nb_primes
                product = i * j

    print(product)
