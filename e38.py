"""
The largest 1 to 9 pandigital 9-digit number is inferior than 9999,
which gives us an upper limit

Down here is a solution by hand:
The number to beat is 918273645. This means that our "starting number" (like 192 in the example) should begin with a 9.
Observe: 9[0-9] will have too few or too many digits (8 or 11)
Observe: 9[0-9][0-9] wiil have too few or too many digits (7 or 11)
Observe: larger than 100000 won't work, too few or too many digits.

Conclusion:
The candidate starting number must be in the 9[0-9][0-9][0-9] series.



Observe: the starting number must contain only different digits and no zeroes.
Observe: a 1 in the starting number is also not good as it will be in the *1 answer and the *2 answer (1[8-9]xxx).

9[5-9][2-9][2-9] * 2 = 19xxx. Contains a 9. Not good.
94[2-9][2-9] * 2 = 18[8-9]xx. Contains a 9 or a double 8. Not good.


Still possible candidates: 9[2-3][2-7][2-7]
937[2-7] * 2 = 187xx. Contains a 7 (also in *1). Not good.
936[2-7] simply does not yield a pandigital answer.
935[2-7] * 2 = 187[0-1]x. Contains a 0 or a double 1. Not good.
934[2-7] * 2 = 186[8-9]x. Contains a 9 or a double 8. Not good.

933[2-7] can't work because of double 3.

Try 9327:
9327 * 1 =  9327
9327 * 2 = 18654

That's it!
"""
from collections import Counter


def pandigital(n):
    concatenation = ""
    i = 1
    while len(concatenation) < 9:
        concatenation += str(n*i)
        i += 1
    return int(concatenation)


def is_pandigital(n):
    if sorted(Counter(str(n)).elements()) == sorted(Counter("123456789")):
        return True
    return False


limit = 10000
max_pandigital = 123456789
for x in range(1, limit):
    pandi_number = pandigital(x)
    if is_pandigital(pandi_number) and pandi_number > max_pandigital:
        max_pandigital = pandi_number

print(max_pandigital)
