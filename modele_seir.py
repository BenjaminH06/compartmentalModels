import matplotlib.pyplot as plt
import numpy as np
alpha = float(input('Rentrez la valeur de alpha / taux dincubation  : '))
beta = float(input('Rentrez la valeur de beta / taux de transmission : '))
nu = float(input('Rentrez la valeur de nu / taux de naissance : '))
gamma = float(input('Rentrez la valeur de gamma / taux de guerison : '))
mu = float(input('Rentrez la valeur de mu / mortalité population : '))
s0 = float(input('Rentrez la valeur de s0 : '))
e0 = float(input('Rentrez la valeur de e0 : '))
i0 = float(input('Rentrez la valeur de i0 : '))
r0 = float(input('Rentrez la valeur de r0 : '))
deltaT = 0.1
temps = 100
t = 0

rn = r0
en = e0
In = i0
sn = s0
n = rn + en + In + sn
S = [s0]
E = [e0]
I = [i0]
R = [r0]
N = [n]
T = [t]
while(t < temps):
    
    sn = (-(beta) * sn * In + nu *  n - sn * mu) * deltaT + sn
    
    en = (beta * sn * In - alpha * en - mu * en) * deltaT + en
    
    In = (alpha * en - gamma * In - mu * In) * deltaT + In
    
    rn = (gamma * In - rn * mu) * deltaT + rn
    
    n =  sn + en + In + rn 
    
    t += deltaT
    
    S = S + [sn]
    E = E + [en]
    I = I + [In]
    R = R + [rn]
    T = T + [t]
    N = N + [n]

plt.plot(T, S, label = "Sain")
plt.plot(T, E, label = "Exposé")
plt.plot(T, I, label = "Infecté")
plt.plot(T, R, label = "Retiré")
plt.plot(T, N, label = "Population")
plt.xlabel('$temps$', fontsize = 15)
plt.ylabel('$population$', fontsize = 15)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()