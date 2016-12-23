x = 1
y = 1
i = 3


while len(str(x + y)) < 1000:
    x, y = y, (x + y)
    i += 1

print(i)