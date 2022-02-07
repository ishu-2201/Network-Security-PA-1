import random
import string
import pandas as pd

# To given Hamming Distances for given DES rounds of distict two plain text and single key


def helperhd(rounds1, rounds2, ihd):
    y = [0]
    for i in range(16):
        hd = 0
        for k in range(2):
            for j in range(32):
                if rounds1[i][k][j] != rounds2[i][k][j]:
                    hd += 1
        y.append(hd)
    return y

# It plots the box plot for distict Rounds


def makeplot(keys, text):
    df = pd.DataFrame()
    for i in range(1, 6):
        r1, rounds1 = d.encrypt(keys[0], text)
        r2, rounds2 = d.encrypt(keys[i], text)
        y = helperhd(rounds1, rounds2, i)
        df['HD'+str(i)] = y
    df = df.T
    boxplot = df.boxplot()
    boxplot.set_xlabel("Rounds")
    boxplot.set_ylabel("Hamming Distances")
    print('Distinct Keys and Single Plain Text')
    print(boxplot)


# Generating random Plain Text
plaintext = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
# distinct keys with distinct Hamming Distances
keys = ['Hello da', 'Jello da', 'Hfllo da', 'Hfllo ea', 'Jfllo ea', 'Kfllo ea']
#   x           1 HD        2 HD.      3 HD.        4 HD        5 HD     -> corresponding to x

d = des()

makeplot(keys, plaintext)
