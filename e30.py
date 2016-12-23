def digit_nth_powers(puissance=4):
    nb_digits_max = 2
    while nb_digits_max * pow(9, puissance) >= pow(10, nb_digits_max):
        nb_digits_max += 1
    limit_max = nb_digits_max * pow(9, puissance)

    total_sum = 0
    for n in range(10, limit_max+1):
        sum = 0
        for i in str(n):
            sum += pow(int(i), puissance)

        if sum == n:
            total_sum += sum

    return total_sum


if __name__ == "__main__":
    print(digit_nth_powers(5))
