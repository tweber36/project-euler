import fractions

num_prod = 1
den_prod = 1
for i in range(1, 10):
    for d in range(1, i):
        for n in range(1, d):
            if (n*10 + i) * d == (i*10 + d) * n:
                num_prod *= n
                den_prod *= d

resultat = fractions.Fraction(num_prod, den_prod)

print(resultat)