def is_abundant(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            sum += i
    return sum > n

def non_abundant_sums(limit):
    abn = set()
    sum = 0
    for n in range(1, limit + 1):
        if is_abundant(n):
            abn.add(n)
        if not any((n-a in abn) for a in abn):
            sum += n
    return sum

if __name__ == '__main__':
    resultat = non_abundant_sums(28123)
    print(resultat)