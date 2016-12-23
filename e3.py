def first_prime(n):
    i = 2
    while n % i != 0: 
        i += 1
    if i < n: 
        print(i)
        return first_prime(n/i)
    else: 
        return n

if __name__ == "__main__":
    print(first_prime(600851475143))
