import numpy as np
import matplotlib.pyplot as plt

t_step = 0.01
t_max = 10
t_min = 1
z0 = 0

t = np.arange(t_min, t_max, t_step)

c2 = 0
rho0 = 1
k = t_min - (t_step * 10)
k = 0
xi = 0

# Change density
for rho0 in np.linspace(0, 10, 20):
    V = np.pi * rho0 * (-7*z0**3 - (k - t)**2 * (t - 6*(t+z0) * xi + k * (-1 + 6 * xi))) / (3 * (k - t)**3)
    
    plt.plot(t, V)
    plt.scatter(0,0, marker='', label=f'$\\rho$ = {np.round(rho0, 2)}')
    plt.legend()
    plt.title('Constant density')
    plt.show()

# Change z0
rho0 = 1
for z0 in np.linspace(-10, 10, 20):
    V = np.pi * rho0 * (-7*z0**3 - (k - t)**2 * (t - 6*(t+z0) * xi + k * (-1 + 6 * xi))) / (3 * (k - t)**3)
    
    plt.plot(t, V)
    plt.scatter(0,0, marker='', label=f'z0 = {np.round(z0, 2)}')
    plt.legend()
    plt.title('Constant density')
    plt.show()

