def collatz_length(limit):
    collatz = []
    maxLength = 0
    maxStartNumber = 0

    for i in range(1, limit+1):
        collatz.append(i)
        counter = 1

        while collatz[-1] != 1:
            if collatz[-1] % 2 == 0:
                collatz.append(collatz[-1]/2)
            else: 
                collatz.append(3*collatz[-1]+1)
            counter += 1 

        if counter > maxLength:
            maxLength = counter
            maxStartNumber = i


    return maxStartNumber, maxLength


if __name__ == "__main__":
    n, l = collatz_length(1000000)

    print n, l


