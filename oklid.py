import math

def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2)

noktalar = [(1, 2), (4, 6), (7, 8), (2, 1), (9, 5)]

mesafeler = []

for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

min_mesafe = min(mesafeler)
print("Minimum Öklid mesafesi:", min_mesafe)