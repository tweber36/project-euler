def next_perm(n):
    numbers = [int(i) for i in str(n)]
    i = -1
    while i > - len(numbers):
        if numbers[i] <= numbers[i-1]:
            i -= 1
        else:
            first_part = numbers[:i-1]
            pivot = numbers[i-1]
            last_part = numbers[i:]
            first_part.append(min([x for x in last_part if x > pivot]))
            last_part.append(pivot)
            last_part.remove(first_part[-1])
            last_part.sort()
            numbers = first_part + last_part
            break
    number_str = ""
    for i in numbers:
        number_str += str(i)
    return number_str

nb_perms = 0
number = '0123456789'
while nb_perms < 999999:
    number = next_perm(number)
    nb_perms += 1

print(number)


