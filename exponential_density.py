import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expi

# Functions
def dirac_delta(arr, x):
    tol = 1e-150
    out = np.zeros_like(arr)
    out[np.abs(x) <= tol] = 0
    return out

def dirac_delta_prime(t):
    return 1

def plot_labels():
    plt.xlabel('t')
    # plt.axvline(tprime + 2*e, linestyle=':', color='black')#, label='Signal reaches observer')
    plt.axvline(tprime -2*z0, linestyle='--', color='black')#, label='Signal from density reaches observer')
    plt.legend()

# Time
t = np.linspace(1, 5, 10000)

# Coefficients and initial variables
a = 1
b = -1
d = 1
c1 = 1
c2 = 1
z0 = -1
tprime = 0
e = 0.5
xi = 1

# The z values
z = np.linspace(-2, 2, 1000)

# Density
rho = np.empty_like(z)
rho[z < z0] = a*np.exp(b*z[z < z0]) + d
rho[z > z0] = 0

if a*np.exp(b*z0) + d < 0:
    raise Exception('Denisty must not be negative anywhere')

# Potential
phi = np.empty_like(z)

phi[z < z0] = 4 * np.pi * a/b**2 * np.exp(b*z[z < z0]) + 2 * np.pi * d * z[z < z0]**2 + c1 * z[z < z0] + c2
phi[z > z0] = (4*np.pi*a / b*np.exp(b*z0) + 4*np.pi*d*z0 + c1)*z[z > z0] + 4*np.pi*a / b**2*np.exp(b*z0) + 2*np.pi*d*z0**2 + c1*z0 + c2 - (4*np.pi*a / b*np.exp(b*z0) + 4*np.pi*d*z0 + c1)*z0

# B
def B(t):
    B_before = np.zeros_like(t)
    B_after = (np.pi * (2 * a * ( - np.exp(1 / 2 * b * ( - t + tprime)) + np.exp(b * z0)) + b * d * (t - tprime + 2 * z0)))
    
    B = B_before * np.heaviside(t - tprime -2*e, 0) * np.heaviside(-t + tprime - 2*z0, 0) + B_after * np.heaviside(t - tprime + 2*z0, 0)
    return B

# A
def A(t):
    A = 1 / (12 * b**3 * (t - tprime)) * (6 * a * np.pi * ( - 8 * np.exp(1 / 2 * b * ( - t + tprime)) + np.exp(b * z0) * (8 + b * (4 + b * (t - tprime - 2 * z0)) * (t - tprime - 2 * z0))) + b**3 * (12 * c2 * (t - tprime) + d * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3))) * np.heaviside((t - tprime) / 2 - np.abs(z0), 0.5) + (c2 - 2 * d * np.pi * z0**2 - (4 * a * np.exp(b * z0) * np.pi * ( - 1 + b * z0)) / b**2) * np.heaviside(1 / 2 * ( - t + tprime) + np.abs(z0), 0.5)
    return A

# Derivatives of A
# A_t
def A_t(t):
    A_t = (- c2 + 2 * d * np.pi * z0**2 + (4 * a * np.exp(b * z0) * np.pi * ( - 1 + b * z0)) / b**2) * dirac_delta(t, t - tprime - 2 * np.abs(z0)) + 1 / (12 * b**3 * (t - tprime)) * (6 * a * np.pi * ( - 8 * np.exp(1 / 2 * b * ( - t + tprime)) + np.exp(b * z0) * (8 + b * (4 + b * (t - tprime - 2 * z0)) * (t - tprime - 2 * z0))) + b**3 * (12 * c2 * (t - tprime) + d * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3))) * dirac_delta(t, t - tprime - 2 * np.abs(z0)) + 1 / (6 * b**3 * (t - tprime)**2) * np.pi * (b**3 * d * (t - tprime - z0) * (t - tprime + 2 * z0)**2 + 3 * a * (4 * np.exp(1 / 2 * b * ( - t + tprime)) * (2 + b * t - b * tprime) + np.exp(b * z0) * ( - 8 + b * (b * (t - tprime)**2 + 8 * z0 - 4 * b * z0**2)))) * np.heaviside(t - tprime - 2 * np.abs(z0), 0.5)
    return A_t

# A_t tprime
def A_tt(t):
    A_tt =  - 1 / (2 * b**2 * (t - tprime)) * (8 * a * (np.exp(1 / 2 * b * ( - t + tprime)) + np.exp(b * z0)) * np.pi + b * (4 * b * c2 - 4 * a * np.exp(b * z0) * np.pi * ( - t + tprime + 2 * z0) + b * d * np.pi * ((t - tprime)**2 + 4 * (t - tprime) * z0 - 4 * z0**2))) * dirac_delta(t, t - tprime - 2 * np.abs(z0)) + 1 / (6 * b**3 * (t - tprime)**2) * (6 * a * np.pi * ( - 8 * np.exp(1 / 2 * b * ( - t + tprime)) + np.exp(b * z0) * (8 + b * (4 + b * (t - tprime - 2 * z0)) * (t - tprime - 2 * z0))) + b**3 * (12 * c2 * (t - tprime) + d * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3))) * dirac_delta(t, t - tprime - 2 * np.abs(z0)) + 1 / (6 * b**3 * (t - tprime)**3) * np.pi * (b**3 * d * ( - (t - tprime)**3 - 8 * z0**3) + 6 * a * (np.exp(1 / 2 * b * ( - t + tprime)) * (8 + b * (t - tprime) * (4 + b * t - b * tprime)) - 4 * np.exp(b * z0) * (2 + b * z0 * ( - 2 + b * z0)))) * np.heaviside(t - tprime - 2 * np.abs(z0), 1) + (c2 - 2 * d * np.pi * z0**2 - (4 * a * np.exp(b * z0) * np.pi * ( - 1 + b * z0)) / b**2) * dirac_delta_prime(t - tprime - 2 * np.abs(z0)) - 1 / (12 * b**3 * (t - tprime)) * (6 * a * np.pi * ( - 8 * np.exp(1 / 2 * b * ( - t + tprime)) + np.exp(b * z0) * (8 + b * (4 + b * (t - tprime - 2 * z0)) * (t - tprime - 2 * z0))) + b**3 * (12 * c2 * (t - tprime) + d * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3))) * dirac_delta_prime(t - tprime - 2 * np.abs(z0))
    return A_tt

# V
def V(t):
    V = -2 * A_tt(t) - 2 * xi * B(t)
    return V


# # Plots
# # Denisty and potential
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()

# ax1.plot(z, rho, color='red')
# ax1.tick_params(axis='y', labelcolor='red')

# ax2.plot(0, 0, label='$\\rho$', color='red')
# ax2.plot(z, phi, label='$\Phi$', color='blue')

# ax2.tick_params(axis='y', labelcolor='blue')
# plt.title('Density of the spacetime and gravitational potential')
# plt.xlabel('z')
# plt.legend()
# plt.show()

# # A
# fig, ax = plt.subplots()
# plt.title(f'$A$ against time (t) (t\'={tprime})')
# plt.plot(t, A(t), label='A')
# plot_labels()
# plt.show()

# # A_t
# fig, ax = plt.subplots()
# plt.title('$\partial_{t\'}A$ against time'+f' (t) (t\'={tprime})')
# plt.plot(t, A_t(t), label='$\partial_{t\'}A$')
# plot_labels()
# plt.show()

# # A_tt
# fig, ax = plt.subplots()
# plt.title('$\partial_{tt\'}A$ against time'+f' (t) (t\'={tprime})')
# plt.plot(t, A_tt(t), label='$\partial_{tt\'}A$')
# plot_labels()
# plt.show()

# # B
# fig, ax1 = plt.subplots()
# plt.plot(t, B(t), label='B')
# plt.title(f'B against time (t) (t\'={tprime})')
# plot_labels()
# plt.show()

# # V


# t = np.linspace(1,11, 10000)


# # Grows to right b >1

# fig, ax = plt.subplots()
# b = 1

# d = 0
# ax.plot(t, V(t), label=f'd = {d}', color='tab:blue')

# d = 1
# ax.plot(t, V(t), label=f'd = {d}', color='tab:blue', linestyle=':')

# axin = ax.inset_axes([0.12, 0.1, 0.3, 0.3])

# plt.title(f'V against time (t) (t\'={tprime}) with b={b}')
# plt.xlabel('t')
# # plt.axvline(tprime + 2*e, linestyle=':', color='black')#, label='Signal reaches observer')
# plt.axvline(tprime -2*z0, linestyle='--', color='black')#, label='Signal from density reaches observer')
# plt.legend(loc=1)


# tshort = np.linspace(1.7, 2, 1000)
# d = 0
# axin.plot(tshort, V(tshort), label=f'd = {d}', color='tab:blue')

# d = 1
# axin.plot(tshort, V(tshort), label=f'd = {d}', color='tab:blue', linestyle=':')


# plt.show()





q=1
tau1 = 1
tau2 = 2


def psi_pulse(t):
    
    K1=np.heaviside(t + 2 * z0 - tau1, 1)
    K2=np.heaviside(t + 2 * z0 - tau2, 1) 
    Ka1=np.heaviside( - t - 2 * z0 + tau1, 1) 
    Ka2=np.heaviside( - t - 2 * z0 + tau2, 1) 
    T=(1)/(4 * z0**2) * K1 * Ka2 
    D1=(dirac_delta(t, t + 2 * z0 - tau1))/(t - tau1) 
    D2=(dirac_delta(t, t + 2 * z0 - tau2))/( - t + tau2) 
    E1=expi((1)/(2) * b * ( - t + tau1)) 
    E2=expi((1)/(2) * b * ( - t + tau2))
    
    M1=d * np.pi * q * (t + 3 * z0 - (4 * z0**3)/((t - tau1)**2) - tau1) - (3 * a * e**(b * z0) * np.pi * q * ( - 8 + 8 * b * z0 + 4 * e**( - (1)/(2) * b * (t + 2 * z0 - tau1)) * (2 + b * (t - tau1)) + b**2 * (t**2 - 4 * z0**2 - 2 * t * tau1 + tau1**2)))/(b**3 * (t - tau1)**2)
    M2=d * np.pi * q * (t + 3 * z0 - (4 * z0**3)/((t - tau2)**2) - tau2) + (3 * a * e**(b * z0) * np.pi * q * ( - 8 + 8 * b * z0 + 4 * e**( - (1)/(2) * b * (t + 2 * z0 - tau2)) * (2 + b * (t - tau2)) + b**2 * (t**2 - 4 * z0**2 - 2 * t * tau2 + tau2**2)))/(b**3 * (t - tau2)**2)
    
    L1=np.zeros_like(t)
    L2=np.zeros_like(t)
    
    L1[t>tau1]=8 * a*b * d * K1[t>tau1] * (t[t>tau1] + 2 * z0 - tau1 + 2 * z0 * np.log(((t[t>tau1] - tau1)/( - 2 * z0)))) 
    L1[t<tau1]=Ka1[t<tau1] * ( - expi(b * z0) + E1[t<tau1] + e**(b * z0) * np.log(((2 * z0)/( - t[t<tau1] + tau1))))
    
    L2[t>tau2]=8 * a*b * d * K2[t>tau2] * (t[t>tau2] + 2 * z0 - tau2 + 2 * z0 * np.log(((t[t>tau2] - tau2)/( - 2 * z0))))
    L2[t<tau2]=Ka2[t<tau2] * ( - expi(b * z0) + E2[t<tau2] + e**(b * z0) * np.log(((2 * z0)/( - t[t<tau2] + tau2))))
    
    log=np.zeros_like(t)
    
    log[(t<tau1) * (t<tau2)] = (E1[(t<tau1) * (t<tau2)] - E2[(t<tau1) * (t<tau2)] - L1[(t<tau1) * (t<tau2)] + L2[(t<tau1) * (t<tau2)] + np.exp(b * z0) * np.log(( - t[(t<tau1) * (t<tau2)] + tau2)/( - t[(t<tau1) * (t<tau2)] + tau1)))
    
    log[(t>tau1) * (t>tau2)] = (E1[(t>tau1) * (t>tau2)] - E2[(t>tau1) * (t>tau2)] - L1[(t>tau1) * (t>tau2)] + L2[(t>tau1) * (t>tau2)] + np.exp(b * z0) * np.log(( - t[(t>tau1) * (t>tau2)] + tau2)/( - t[(t>tau1) * (t>tau2)] + tau1)))
    
    
    return - 2 * ((c2 * q + (4 * a * np.exp(b * z0) * np.pi * q)/(b**2) - (4 * a * np.exp(b * z0) * np.pi * q * z0)/(b) - 2 * d * np.pi * q * z0**2) * (dirac_delta(t, t + 2 * z0 - tau1) - dirac_delta(t, t + 2 * z0 - tau2)) + ((d * np.pi * q * t**2 * z0)/(2) + (a * np.exp(b * z0) * np.pi * q)/(b**(34)) + c2 * q * t + (a * np.exp(b * z0) * np.pi * q * t)/(b**(22)) + (d * np.pi * q * t**3)/(12) - (a * np.exp(b * z0) * np.pi * q * z0)/(b**(24)) - d * np.pi * q * t * z0**2 + (2 * d * np.pi * q * z0**3)/(3) + (a * np.exp(b * z0) * np.pi * q * t**2)/(2 * b) - (2 * a * np.exp(b * z0) * np.pi * q * t * z0)/(b) + (2 * a * np.exp(b * z0) * np.pi * q * z0**2)/(b)) * (D1 + D2 + T) + ( - c2 * q - (a * np.exp(b * z0) * np.pi * q)/(b**(22)) - (d * np.pi * q * t**2)/(4) - d * np.pi * q * t * z0 + d * np.pi * q * z0**2 - (a * np.exp(b * z0) * np.pi * q * t)/(b) + (2 * a * np.exp(b * z0) * np.pi * q * z0)/(b)) * (tau1 * D1 + tau2 * D2 + t * T) *  - (d * np.pi * q)/(12) * (tau1**3 * D1 + tau2**3 * D2 + ((t - 4 * z0) * (t + 2 * z0)**2) * T) - (a * np.pi * q * (np.exp( - (1)/(2) * b * (t - tau1)) * D1 + np.exp( - (1)/(2) * b * (t - tau2)) * D2 + (np.exp(b * z0) * (1 - b * z0)) * T)) * (b**(34)) + ((d * np.pi * q * t)/(4) + (d * np.pi * q * z0)/(2) + (a * np.exp(b * z0) * np.pi * q)/(2 * b)) * (tau1**2 * D1 + tau2**2 * D2 + ((t**2 - 4 * z0**2)) * T) + (1)/(6) * (6 * q * ( - tau1 + tau2) - M1 * K1 + M2 * K2 + (6 * d * np.pi * z0 - (6 * np.pi * (a * np.exp(b * z0) + b * d * z0))/(b**2) - (6 * q * (4 * a * np.exp(b * z0) * np.pi - 4 * a * b * np.exp(b * z0) * np.pi * z0 +  b**2 * (c2 - 2 * d * np.pi * z0**2)))/(b**2 * z0) + (6 * (4 * a * np.exp(b * z0) * np.pi - 2 * a * b * np.exp(b * z0) * np.pi * z0 + b**2 * (c2 - d * np.pi * z0**2)))/(b**2 * z0)) * K1 * Ka2)) + (4*a*np.pi * q * xi)/(b) * log



t = np.linspace(1, 4, 10000)

b=1

tau1 = 0
tau2 = 1

for d in np.linspace(0, 10):
    plt.title(d)
    plt.plot(t, psi_pulse(t))
    plt.show()
