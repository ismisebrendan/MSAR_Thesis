import numpy as np
import matplotlib.pyplot as plt

t_step = 0.01
t_max = 10
t_min = 1
z0 = 5

t = np.arange(t_min, t_max, t_step)

k = t_min - (t_step * 10)
k = 0
xi = 0

#
# Linearly varying density
#

print('Linear')

z = np.arange(-10, 10, 0.001)

b = 20
a = -1

c2 = 1


for a in np.linspace(-5, 5, 100):

    rho = b + a * z
    rho[z>z0] = 0

    if (rho < 0).any():
        print('WARNING: Density drops below 0')
       
    
    V = (np.pi * (-56 * b * z0**3-41 * a * z0**4 + 3 * a * (k-t)**2 * ((k-t)**2 - 4 * (k-t-z0) * (k-t+z0) * xi) - 8 * b * (k-t)**2 * (t - 6 * (t+z0) * xi + k * (-1 + 6 * xi))))/(24 * (k-t)**3)
    
    plt.plot(t, V)
    plt.scatter(0,0, marker='', label=f'$\\rho$ = {np.round(a, 2)}z+{np.round(b, 2)}')
    
    
    plt.legend()
    plt.title(f'Linearly varying denisty, b = {b}')
    
    plt.show()
