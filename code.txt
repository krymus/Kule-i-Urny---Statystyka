import random

def losowanie(n):
    urna = [0 for i in range(n)]
    result = [0, 0, 0, 0, 0]
    result[0] = 0 #Bn
    result[1] = 0 #Un
    result[2]  = 0 #Ln
    result[3]= 0 #Cn
    result[4] = 0 #Dn
    i = 0
    
    while result[4] == 0:

        los = random.randint(0, n-1)
        urna[los] += 1

        if urna[los] == 2 and result[0] == 0:
            result[0] = i + 1

        if i == n-1:
            for j in range(n):
                if urna[j] == 0:
                    result[1] += 1
                elif urna[j] > result[2]:
                    result[2] = urna[j]

        if urna[los] == 1 and i >= n-1:
            for j in range(n):
                if urna[j] == 0:
                    break
                if j == n-1:
                    result[3] = i + 1


        if urna[los] == 2 and i >= 2*n - 1:
            for j in range(n):
                if urna[j] == 1 or urna[j]==0:
                    break
                elif j == n-1:
                    result[4] = i + 1  
  
        i += 1
    
    return result

f = open("wyniki", "x")

for n in range(1000,100001,1000):
    for k in range(50):
        f.write(str(losowanie(n)) + '\n')
        print(n)


f.close()
