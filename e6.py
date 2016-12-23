def square_dif(n):
    sq_sum = 0
    sum_sq = 0

    for i in range(n):
        sum_sq += i*i
        sq_sum += i 

    sq_sum = sq_sum * sq_sum

    diff = sq_sum - sum_sq

    return diff


if __name__ == "__main__":
    print square_dif(101)
