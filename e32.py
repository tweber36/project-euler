def is_pandigital(multiplicand, multiplier, product):
    numbers = [multiplicand, multiplier, product]
    numbers = list("".join(numbers))
    if len(numbers) > 9:
        return False

    if len(set(numbers)) == 9 and "0" not in numbers:
        return True
    else:
        return False


products = []
for i in range(1, 10):
    for j in range(1000, 10000):
        if is_pandigital(str(i), str(j), str(i*j)) and i*j not in products:
            products.append(i*j)
for i in range(10, 100):
    for j in range(100, 1000):
        if is_pandigital(str(i), str(j), str(i*j)) and i*j not in products:
            products.append(i * j)


print(sum(products))