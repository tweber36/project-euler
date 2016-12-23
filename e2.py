def fibo(limit):
    res = [1, 1]
    while res[-1] < limit:
        res.append(res[-1]+res[-2])
    
    return res

if __name__ == "__main__":
    l = 4000000
    fib = fibo(l)
    sum = 0

    for i in range(len(fib)):
        if fib[i] % 2 == 0:
            sum += fib[i]

    print(sum)
