coins_possible = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200


def ways(target, coin_index):
    if coin_index <= 1:
        return 1
    res = 0
    while target >= 0:
        res += ways(target, coin_index-1)
        target -= coins_possible[coin_index-1]
    return res

print(ways(amount, len(coins_possible)))

ways2 = [0]*(amount+1)
ways2[0] = 1
for x in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(x, amount+1):
        ways2[i] += ways2[i-x]

print(ways2[amount])

