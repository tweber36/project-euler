n = 1000000  # Upper limit
palindromes = []


def is_palindrome(num):
    return str(num) == str(num)[::-1]


for i in range(1, n+1):
    if is_palindrome(i):
        binary = bin(i)
        if is_palindrome(int(binary[2:])):
            palindromes.extend((i, int(str(i)[::-1])))

print(sum(palindromes) / 2)
