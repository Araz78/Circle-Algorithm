import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
#=========================================== input value of r
r  = int(input("Please Enter Value of r: "))
#=========================================== Calculate the value of P0
P0 = 1 - r
#=========================================== Insert the values ​​of X_k, Y_k, P_k
X_k = []
X_k.append(0)

Y_k = []
Y_k.append(r)

P_k = []
P_k.append(P0)

i = 0
while X_k[i] <= Y_k[i]:
    if P_k[i] < 0:
        new_pk = (P_k[i] + ((2 * (X_k[i] + 1)) + 1))
        P_k.append(new_pk)
        X_k.append(1 + X_k[i])
        Y_k.append(Y_k[i])
        i+=1

    else:
        new_pk = ((P_k[i] + ((2 * (X_k[i] + 1)) + 1)) - (2 * (Y_k[i] - 1)))
        P_k.append(new_pk)
        X_k.append(1 + X_k[i])
        Y_k.append(Y_k[i] - 1)
        i+=1
#=========================================== Clear extra numbers and negative X_k and Y_k
xk = X_k[i]
yk = Y_k[i]
pk = P_k[i]
X_k.remove(xk)
Y_k.remove(yk)
P_k.remove(pk)

X_k_negative = [ -x for x in X_k]
Y_k_negative = [ -y for y in Y_k]
#=========================================== Draw First Quarter
plt.plot(X_k, Y_k, 'o', color='red')
plt.savefig('First Quarter.png')
#=========================================== Draw Second Quarter
plt.plot(Y_k, X_k, 'o', color='red')
plt.savefig('Second Quarter.png')
#=========================================== Draw Third Quarter
plt.plot(Y_k_negative, X_k, 'o', color='red')
plt.savefig('Third Quarter.png')
#=========================================== Draw Fourth Quarter
plt.plot(X_k_negative, Y_k, 'o', color='red')
plt.savefig('Fourth Quarter.png')
#=========================================== Draw Fifth Quarter
plt.plot(X_k_negative, Y_k_negative, 'o', color='red')
plt.savefig('Fifth Quarter.png')
#=========================================== Draw Sixth Quarter
plt.plot(Y_k_negative, X_k_negative, 'o', color='red')
plt.savefig('Sixth Quarter.png')
#=========================================== Draw Seventh Quarter
plt.plot(Y_k, X_k_negative, 'o', color='red')
plt.savefig('Seventh Quarter.png')
#=========================================== Draw Eighth Quarter
plt.plot(X_k, Y_k_negative, 'o', color='red')
plt.savefig('Eighth Quarter.png')
#=========================================== Draw All Quarter
plt.plot(X_k, Y_k,Y_k,X_k,Y_k_negative,X_k,X_k_negative,Y_k,X_k_negative,Y_k_negative,Y_k_negative,X_k_negative,Y_k,X_k_negative,X_k,Y_k_negative, 'o', color='red')
plt.savefig('All Quarter.png')
# Araz Alinejad
