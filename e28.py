def sum_diagonals(size=3):
    if size < 2 or size%2 == 0:
        raise ValueError("""Impossible de créer la spirale avec une taille inférieure à 2 ou un nombre pair de
                            colonnes""")
    else:
        sum = 1
        for i in range(3, size+1, 2):
            sum += 4*i**2 - 6*(i-1)
        return sum

if __name__ == "__main__":
    print(sum_diagonals(1001))