import matplotlib.pyplot as plt
import math

f = open("wyniki", "r")

Bn = []
avgBn = []
Un = []
avgUn = []
Ln = []
avgLn = []
Cn = []
avgCn = []
Dn = []
avgDn = []
DnCn = []
avgDnCn = []
n = []
navg = []

for x in f:
    split = x.split()
    Bn.append(int(split[0]))
    Un.append(int(split[1]))
    Ln.append(int(split[2]))
    Cn.append(int(split[3]))
    Dn.append(int(split[4]))
f.close()

for i in range(1000,100001,1000):
    navg.append(i)
    for k in range(50):
        n.append(i)

DnCn = []
for i in range(5000):
    DnCn.append(Dn[i] - Cn[i])

avgbn = 0
avgun = 0
avgln = 0
avgcn = 0
avgdn = 0
avgdncn = 0

for i in range(5001):
    if i != 0 and i % 50 == 0:
        avgBn.append(avgbn/50)
        avgUn.append(avgun/50)
        avgLn.append(avgln/50)
        avgCn.append(avgcn/50)
        avgDn.append(avgdn/50)
        avgDnCn.append(avgdncn/50)
        avgbn = 0
        avgun = 0
        avgln = 0
        avgcn = 0
        avgdn = 0
        avgdncn = 0
    if i == 5000: 
        break
    avgbn += Bn[i]
    avgun += Un[i]
    avgln += Ln[i]
    avgcn += Cn[i]
    avgdn += Dn[i]
    avgdncn += DnCn[i]


iloraz = []
for i in range(100):
    iloraz.append(avgBn[i]/navg[i])

             
iloraz2 = []
for i in range(100):
    iloraz2.append(avgBn[i]/math.sqrt(navg[i]))

'''
iloraz3 = []
for i in range(100):
    iloraz3.append((avgDn[i]/navg[i]/navg[1]))
'''



plt.scatter(navg, iloraz, s = 1)
#plt.scatter(navg, iloraz3, s = 1, color = 'green')
plt.scatter(navg, iloraz2, s = 1, color = 'red')
#plt.ylabel('un/n')
plt.xlabel('n')
plt.show()
