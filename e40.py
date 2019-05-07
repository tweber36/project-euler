"""
An irrational decimal fraction is created
by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


def calculate_nth_digit(n):
    number_to_add = 1
    digit_index = 0
    while digit_index + len(str(number_to_add)) < n:
        digit_index += len(str(number_to_add))
        number_to_add += 1
    return int(str(number_to_add)[n-digit_index-1])

result = 1
for i in range(7):
    result *= calculate_nth_digit(pow(10, i))

print(result)
