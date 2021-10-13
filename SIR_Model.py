import matplotlib.pyplot as plt
import numpy as np
alpha = float(input('Rentrez la valeur de alpha : '))
beta = float(input('Rentrez la valeur de beta : '))
s0 = float(input('Rentrez la valeur de s0 : '))
i0 = float(input('Rentrez la valeur de i0 : '))
r0 = float(input('Rentrez la valeur de r0 : '))
deltaT = 0.1
temps = 100
t = 0

rn = r0
In = i0
sn = s0
S = [s0]
I = [i0]
R = [r0]
T = [t]
while(t < temps):
    
    rn = beta * In * deltaT + rn
    
    In = deltaT * (alpha * sn * In - beta * In) + In 
    
    sn = sn * (1 - alpha * deltaT * In)
    
    t += deltaT
    
    S = S + [sn]
    I = I + [In]
    R = R + [rn]
    T = T + [t]

plt.plot(T, S)
plt.plot(T, I)
plt.plot(T, R)
plt.xlabel('$temps$', fontsize = 15)
plt.ylabel('$population$', fontsize = 15)
plt.show()