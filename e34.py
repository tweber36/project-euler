import math

factorial_list = [math.factorial(x) for x in range(0, 10)]
result = 0

for i in range(10, 2540161):
    numbers = list(str(i))
    numbers = [int(x) for x in numbers]

    sum_numbers = 0
    for x in numbers:
        sum_numbers += factorial_list[x]

    if sum_numbers == i:
        result += sum_numbers

print(result)
