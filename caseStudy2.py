#import numpy as np
import math
import matplotlib.pyplot as plt

vitesse = [0]*150
vitesseGraph = [0]*150
distanceTotal = [0]*150
for i in range(20,150):
    vitesse[i] = i/3.6
    vitesseGraph[i] = i
    Bat = 54000  # en Wh
    k = 0.239
    R = 0.1  # en ohm
    Ie = 2.5  # en A
    w = vitesse[i] / 0.05  # en rad/s

    F = 0.5 * 0.38 * 1.74 * math.pow(vitesse[i], 2) + 4 * 0.01 * 9.81 * 1548
    Pmeca = F * vitesse[i]
    Cmot = Pmeca / w

    E = k * Ie * w  # en joules
    I = Cmot / (k * Ie)  # en A

    Uentree = E + R * I  # en V
    UGen = E - R * I  # en V

    Pentree = Uentree * I  # puissance W consommée par la batterie pour une vitesse à un instant t
    PPertes = R * math.pow(I, 2)  # pertes Joules en W
    Psortie = Pentree - PPertes

    PGen = UGen * I  # puissance récupérée W par le moteur pour une vitesse à un instant t
    Ptotal = 0
    heureTotal = 0
    PtempEntree = 0
    PtempSortie = 0
    PtempGen = 0
    PtotalTemp = 0
    while(Bat >0 ):
        PtempEntree = 0.167 * Pentree
        PtempGen = 0.0167 * PGen
        heureTotal += 0.11
        PtotalTemp = PtempEntree - PtempGen
        Ptotal += PtempEntree - PtempGen
        if(Bat - PtotalTemp >= 0):
            distanceTotal[i] += vitesse[i] * 660
            Bat -= PtotalTemp
        else:
            break
    print("vitesse: ", vitesse[i])
    print("distance Totale : ", distanceTotal[i])
    print("Ptotal: ", Ptotal)

#distance en fonctino de la vitesse décrément log
plt.plot(vitesseGraph[20:], distanceTotal[20:])
plt.xlabel('vitesse en km/h')
plt.ylabel('distance en km')
plt.legend(['distance parcourue en fonction de la vitesse'])
plt.show()
