def decomposition_nombre(n):
    liste = []
    
    liste = map(int, str(n))
    liste.reverse()

    return liste


def calcul_puissance(l):
    liste = [1, ]
    liste_temp = list(liste)
    retenue = 0
    somme = 0

    for i in range(1, l+1):
        for j in range(len(liste)):
            decompo = decomposition_nombre(2*liste[j])
            liste_temp[j] = decompo[0] + retenue

            if len(decompo) > 1:
                retenue = decompo[1]
            else:
                retenue = 0

            if j == len(liste)-1 and retenue > 0:
                liste_temp.append(retenue)
                retenue = 0

        liste = liste_temp

    for x in liste:
        somme += x
    
    print liste
    return somme


if __name__ == "__main__":
    print calcul_puissance(1000)
