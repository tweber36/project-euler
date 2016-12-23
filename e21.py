def sum_of_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def amicable_numbers(limit):
    sum = 0
    for i in range(1, limit+1):
       if sum_of_divisors(sum_of_divisors(i)) == i and i != sum_of_divisors(i):
           sum += i
    return sum

print(amicable_numbers(10000))

