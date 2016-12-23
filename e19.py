
def is_leap_year(x):
    if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
        return 29
    else:
        return 28

def number_of_days(x):
    return [31, is_leap_year(x), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sundays_first = 0
last_sunday = 0

for i in range(1900, 2001):
    for j in number_of_days(i):
        last_sunday += -(j % 7)
        if last_sunday <= -7:
            last_sunday += 7
        if last_sunday == -6 and i >= 1901:
            sundays_first += 1
        print(last_sunday, sundays_first)

print(sundays_first)
