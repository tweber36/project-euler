def deplacement(n):
    poids = []

    for i in range(n+1):
        poids.append((n+1)*[1, ])

    for i in range(n+1):
        for j in range(i+1):
            if j == 0:
                poids[i][0] = 1
            elif j-i == 0:
                poids[0][i] = 1
            else:
                poids[i-j][j] = poids[i-j-1][j] + poids[i-j][j-1]
    
    for j in range(1, n+1):
        for i in range(n, j-1, -1):

            poids[i][j+n-i] = poids[i-1][j+n-i] + poids[i][j+n-i-1]
    
    return poids[n][n]

if __name__ == "__main__":
    print deplacement(20)
