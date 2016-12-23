def is_palindrome(x, y):
    n = x * y
    if n == int(str(n)[::-1]):
        return 1
    else:
        return 0

def max_palindrome(limit):
    max_pal = 0
    for x in range(limit):
        for y in range(limit):
            if is_palindrome(x, y) and x*y > max_pal:
                max_pal = x*y

    return max_pal

if __name__ == "__main__":
    print(max_palindrome(999))
    
