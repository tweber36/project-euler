def cycle_length(n):
    restes = []
    reste = 1

    while reste not in restes:
        restes.append(reste)
        reste = (10 * reste) % n
        print(restes)

    return len(restes) - restes.index(reste)

if __name__ == '__main__':
    longest = 0
    result = 0
    for i in range(10000, 1, -1):
        if i%2 != 0 and i%5 != 0:
            length = cycle_length(i)
            if length > longest:
                longest = length
                result = i
            if longest != 0 and i < longest:
                break

    print(result)