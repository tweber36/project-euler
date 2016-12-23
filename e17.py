numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', \
           'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', \
           'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def numbers_of_letters(x):
    written = ""
    result = 0
    hundreds = x // 100
    tens = (x % 100) // 10
    units = (x % 100) % 10

    if hundreds >= 1:
        result += len(numbers[hundreds - 1]) + 7
        written += numbers[hundreds - 1] + " hundred"
        if (x % 100) != 0:
            result += 3
            written += " and"

    if tens >= 2:
        result += len(numbers[tens + 17])
        written += " " + numbers[tens + 17]
        if units > 0:
            result += len(numbers[units - 1])
            written += " " + numbers[units - 1]
    elif tens < 2 and (x % 100) > 0:
        result += len(numbers[(x % 100) - 1])
        written += " " + numbers[(x % 100) - 1]

    print(written)
    return result

def sum_letters(limit):
    i = 1
    sum = 0
    while i < limit:
        sum += numbers_of_letters(i)
        i += 1
    return sum

if __name__ == "__main__":
    print(numbers_of_letters(26))
    print(sum_letters(1000) + 11)