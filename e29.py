def distinct_powers(a_max=5, b_max=5):
    distinct_numbers = []

    for a in range(2, a_max+1):
        for b in range(2, b_max+1):
            distinct_numbers.append(pow(a,b))

    return len(set(distinct_numbers))


if __name__ == "__main__":
    print(distinct_powers(100,100))
