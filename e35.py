n = 1000000  # Upper limit
circular_primes = set()
# First, determine the list of non-prime numbers up to n
# using multiples (Sieve array of Eratosthenes)
not_primes = set()
for i in range(2, n):
    if i in not_primes:
        continue
    multiplier = i
    while i*multiplier <= n:
        not_primes.add(i*multiplier)
        multiplier += 1

# Then, the list of primes up to n is the list of all numbers
# minus the non-prime numbers
primes = set(range(2, n)).difference(not_primes)

# For each prime, check if circular
for i in primes:
    # Explicit all the rotations of the digits
    rotations_list = set(str(i)[x:] + str(i)[:x] for x in range(len(str(i))))

    is_circular = True
    for x in rotations_list:
        if int(x) not in primes:
            is_circular = False
            break

    # Check if already in results to avoiding duplication
    if is_circular and i not in circular_primes:
        circular_primes.update(rotations_list)

print(len(circular_primes))
