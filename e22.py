with open('e22_names.txt', 'r') as fichier_noms:
    texte = fichier_noms.read()
    liste_noms = texte.split(',')
    liste_noms.sort()


def value_name(name):
    value = 0
    for char in name:
        if char == '"':
            pass
        else:
            value += ord(char) - 64
    return value

def name_score(name_list, name):
    return (name_list.index(name) + 1) * value_name(name)


if __name__ == '__main__':
    score = 0
    for name in liste_noms:
        score += name_score(liste_noms, name)
    print(score)