def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


def calculate_sum_factorial(n):
    sum = 0
    for char in str(factorial(n)):
        sum += int(char)
    return sum

if __name__ == "__main__":
    print(calculate_sum_factorial(100))