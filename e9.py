from math import *

def pythagorean_triplet(sum):
    for a in range(1, int(sum/2)):
        for b in range(a+1, int(sum/2)+1):
            c = sqrt(a*a + b*b)
            if c.is_integer() and a+b+c == sum:
                return a, b, int(c)
    return 0, 0, 0

if __name__ == "__main__":
    a, b, c = pythagorean_triplet(1000)

    print a, b, c
    print a*b*c

