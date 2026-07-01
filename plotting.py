import numpy as np
import matplotlib.pyplot as plt

#
# Plot for constant density
#

print('Constant')

t_step = 0.01
t_max = 10
t_min = 0
z0 = 0

t = np.arange(t_min, t_max, t_step)

c2 = 0
rho0 = 1
k = t_min - (t_step * 10)
k = -2
xi = 0.1

# Plot A for different z0
# for i in np.arange(-5, 5, 0.1):

#     z0 = i        
A = c2 + rho0 * np.pi * ((k - t)**3 - 6*(k - t)**2 * z0 + 12*(-k + t) * z0**2 - 7*z0**3) / (12 * (k - t))
    
plt.plot(t, A, label='A')
plt.xlabel('Time')


# Plot A,tt'
A_tt = rho0 * np.pi * (-(k - t)**3 + 7*z0**3) / (6 * (k-t)**3)

plt.plot(t, A_tt, label="A$_{tt'}$")

# V
V = np.pi * rho0 * (-7*z0**3 - (k - t)**2 * (t - 6*(t+z0) * xi + k * (-1 + 6 * xi))) / (3 * (k - t)**3)

plt.plot(t, V, label='V')
plt.legend()
plt.title('Constant density')
plt.show()


#
# Linearly varying density
#

print('Linear')

z = np.arange(-10, 10, 0.001)

b = 20
a = -5

rho = b + a * z
rho[z>z0] = 0

if (rho < 0).any():
    print('WARNING: Density drops below 0')


A = (96 * c2 * (k-t) + 8 * b * np.pi * ((k-t)**3 - 6 * (k-t)**2 * z0 + 12 * (-k+t) * z0**2 - 7 * z0**3) + a * np.pi * ((k-t)**4 - 24 * (k-t)**2 * z0**2 + 64 * (-k+t) * z0**3 - 41 * z0**4)) /(96 * (k-t))

plt.plot(t, A, label='A')

A_tt = (np.pi * (-8 * b * (k-t)**3 - 3 * a * (k-t)**4 + 56 * b * z0**3 + 41 * a * z0**4))/(48 * (k-t)**3)

plt.plot(t, A_tt, label="A$_{tt'}$")


V = (np.pi * (-56 * b * z0**3-41 * a * z0**4 + 3 * a * (k-t)**2 * ((k-t)**2 - 4 * (k-t-z0) * (k-t+z0) * xi) - 8 * b * (k-t)**2 * (t - 6 * (t+z0) * xi + k * (-1 + 6 * xi))))/(24 * (k-t)**3)

plt.plot(t, V, label='V')


plt.legend()
plt.title('Linearly varying denisty')

plt.show()

#
# Quadraticaly varying density
#

print('Quadratic')

c = 1
b = 2
a = 1

rho = c + b * z + a * z**2
rho[z>z0] = 0

if (rho < 0).any():
    print('WARNING: Density drops below 0')


A = -1/(1920*(k-t))*(-1920*c2*(k-t)-(k-t)**3*(40*c+(k-t)*(5*b+a*k-a*t))+240*c*(k-t)**2*z0+120*(4*c+b*(k-t))*(k-t)*z0**2+40*(7*c+2*(k-t)*(4*b+a*k-a*t))*z0**3+5*(41*b+48*a*(k-t))*z0**4+161*a*z0**5)

plt.plot(t, A, label='A')

A_tt = (-3*(5*b+2*a*(k-t))*(k-t)**4+205*b*z0**4+161*a*z0**5+40*c*(-(k-t)**3+7*z0**3))/(960*(k-t)**3)

plt.plot(t, A_tt, label="A$_{tt'}$")


V = 1/(480*(k-t)**3)*(5*b*(3*(k-t)**4-41*z0**4-48*np.pi*(k-t)**2*(k-t-z0)*(k-t+z0)*xi)+a*(6*(k-t)**5-161*z0**5-80*np.pi*(k-t)**2*((k-t)**3-z0**3)*xi)+40*c*(-7*z0**3+(k-t)**2*(k-t+24*np.pi*(-k+t+z0)*xi)))

plt.plot(t, V, label='V')


plt.legend()
plt.title('Quadraticaly varying denisty')

plt.show()