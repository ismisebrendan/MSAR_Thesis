import numpy as np
import matplotlib.pyplot as plt

# Functions
def dirac_delta(arr, x):
    tol = 1e-9
    out = np.zeros_like(arr)
    out[np.abs(x) <= tol] = 1
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
a = -1
b = -1
c1 = 0
c2 = 1
z0 = -1
tprime = 0
e = 0.5

# The z values
z = np.linspace(-10, 10, 1000)

# Density
rho = np.empty_like(z)
rho[z < z0] = a*z[z < z0] + b
rho[z > z0] = 0

if a*z0 + b < 0:
    raise Exception('Denisty must not be negative anywhere')

# Potential
phi = np.empty_like(z)
phi[z < z0] = 2/3 * np.pi * a * z[z < z0]**3 + 2 * np.pi * b * z[z < z0]**2 + c1*z[z < z0] + c2
phi[z > z0] = (2 * np.pi * a * z0**2 + 4* np.pi * b * z0 + c1)*z[z > z0] + (-4*np.pi/3 * a * z0**3 - 2* np.pi * b * z0**2 + c2)
# B
def B(t):
    B_before = np.zeros_like(t)
    B_after = (np.pi * (t - tprime + 2 * z0) * (4 * b + a * ( - t + tprime + 2 * z0))) / (4 * (t - tprime))
    
    B = B_before * np.heaviside(t - tprime -2*e, 0) * np.heaviside(-t + tprime - 2*z0, 0) + B_after * np.heaviside(t - tprime + 2*z0, 0)
    return B

# A
def A(t):
    A = (c2 - 2 / 3 * np.pi * z0**2 * (3 * b + 2 * a * z0)) * np.heaviside(1 / 2 * ( - t + tprime) - z0, 0.5) + 1 / (96 * (t - tprime)) * (96 * c2 * (t - tprime) - a * np.pi * (t - tprime - 2 * z0)**3 * (t - tprime + 6 * z0) + 8 * b * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3)) * np.heaviside((t - tprime) / 2 + z0, 0.5)
    return A

# Derivatives of A
# A_t
def A_t(t):
    A_t =  - ((c2 - 2 / 3 * np.pi * z0**2 * (3 * b + 2 * a * z0)) * dirac_delta(t, t - tprime - 2 * np.abs(z0))) + 1 / (96 * (t - tprime)) * (96 * c2 * (t - tprime) - a * np.pi * (t - tprime - 2 * z0)**3 * (t - tprime + 6 * z0) + 8 * b * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3)) * dirac_delta(t, t - tprime - 2 * np.abs(z0)) - (np.pi * (t - tprime + 2 * z0)**2 * (16 * b * ( - t + tprime + z0) + 3 * a * ( - t + tprime + 2 * z0)**2) * np.heaviside(t - tprime - 2 * np.abs(z0), 0.5)) / (96 * (t - tprime)**2)
    return A_t

# A_t tprime
def A_tt(t):
    A_tt = 1 / (12 * (t - tprime)) * ( - 24 * c2 + a * np.pi * ( - t + tprime + 2 * z0)**2 * (t - tprime + 4 * z0) - 6 * b * np.pi * ((t - tprime)**2 + 4 * (t - tprime) * z0 - 4 * z0**2)) * dirac_delta(t, t - tprime - 2 * np.abs(z0)) + 1 / (48 * (t - tprime)**2) * (96 * c2 * (t - tprime) - a * np.pi * (t - tprime - 2 * z0)**3 * (t - tprime + 6 * z0) + 8 * b * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3)) * dirac_delta(t, t - tprime - 2 * np.abs(z0)) + (np.pi * ( - 8 * b * (t - tprime)**3 - 64 * b * z0**3 + 3 * a * ((t - tprime)**4 - 16 * z0**4)) * np.heaviside(t - tprime - 2 * np.abs(z0), 0.5)) / (48 * (t - tprime)**3) + (c2 - 2 / 3 * np.pi * z0**2 * (3 * b + 2 * a * z0)) * dirac_delta_prime(t - tprime - 2 * np.abs(z0)) - 1 / (96 * (t - tprime)) * (96 * c2 * (t - tprime) - a * np.pi * (t - tprime - 2 * z0)**3 * (t - tprime + 6 * z0) + 8 * b * np.pi * ((t - tprime)**3 + 6 * (t - tprime)**2 * z0 + 12 * ( - t + tprime) * z0**2 + 8 * z0**3)) * dirac_delta_prime(t - tprime - 2 * np.abs(z0))
    return A_tt

# V
def V(t, xi):
    V = -2 * A_tt(t) - 2 * xi * B(t)
    return V


# Plots
# Denisty and potential
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(z, rho, color='red')
ax1.tick_params(axis='y', labelcolor='red')

ax2.plot(0, 0, label='$\\rho$', color='red')
ax2.plot(z, phi, label='$\Phi$', color='blue')

ax2.tick_params(axis='y', labelcolor='blue')
plt.title('Density of the spacetime and gravitational potential')
plt.xlabel('z')
plt.legend()
plt.show()

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
# fig, ax = plt.subplots()
# ax.plot(t[t>-2*z0], V(t, 1)[t>-2*z0], label='$\\xi = 1$', color='tab:blue', linestyle=':')
# ax.plot(t, V(t,0), label='$\\xi = 0$', color='tab:blue')
# ax.plot(t[t>-2*z0], V(t,-1)[t>-2*z0], label='$\\xi = -1$', color='tab:blue', linestyle='-.')

# axin = ax.inset_axes([0.65, 0.65, 0.3, 0.3])

# plt.title(f'V against time (t) (t\'={tprime})')
# plot_labels()



# tshort = np.linspace(1.999, 2.001, 10000)

# axin.plot(tshort[tshort>-2*z0], V(tshort, 1)[tshort>-2*z0], label='$\\xi = 1$', color='tab:blue', linestyle=':')
# axin.plot(tshort, V(tshort,0), label='$\\xi = 0$', color='tab:blue')
# axin.plot(tshort[tshort>-2*z0], V(tshort,-1)[tshort>-2*z0], label='$\\xi = -1$', color='tab:blue', linestyle='-.')

# plt.show()


# b = 2
# fig, ax = plt.subplots()
# ax.plot(t[t>-2*z0], V(t, 1)[t>-2*z0], label='$\\xi = 1$', color='tab:blue', linestyle=':')
# ax.plot(t, V(t,0), label='$\\xi = 0$', color='tab:blue')
# ax.plot(t[t>-2*z0], V(t,-1)[t>-2*z0], label='$\\xi = -1$', color='tab:blue', linestyle='-.')

# axin = ax.inset_axes([0.65, 0.65, 0.3, 0.3])

# plt.title(f'V against time (t) (t\'={tprime})')
# plot_labels()



# tshort = np.linspace(1.98, 2.05, 10000)

# axin.plot(tshort[tshort>-2*z0], V(tshort, 1)[tshort>-2*z0], label='$\\xi = 1$', color='tab:blue', linestyle=':')
# axin.plot(tshort, V(tshort,0), label='$\\xi = 0$', color='tab:blue')
# axin.plot(tshort[tshort>-2*z0], V(tshort,-1)[tshort>-2*z0], label='$\\xi = -1$', color='tab:blue', linestyle='-.')

# plt.show()



# Signal stuff
q0 = 1
xi = 1
# tau1 = 3
# tau2 = 3.5

# # Pulse
def q_pulse(t):
    return np.heaviside(t - tau1, 1) * np.heaviside(tau2 - t, 1)

def psi_pulse(t):
    D1 = dirac_delta(t, t+2*z0-tau1) / (t - tau1)
    D2 = dirac_delta(t, t+2*z0-tau2) / (-t + tau2)
    K1 = np.heaviside(t+2*z0-tau1, 1)
    K2 = np.heaviside(t+2*z0-tau2, 1)
    K2a = np.heaviside(-t-2*z0+tau2, 1)
    T = 1/(4 * z0**2) *  K1 * K2a
    L1 = np.zeros_like(t)
    L1[t>tau1] = ( - 8 * b + a * (t[t>tau1] - 2 * z0 - tau1)) * (t[t>tau1] + 2 * z0 - tau1) + 8 * z0 * (2 * b + a * z0) * np.log(( - 2 * z0)/(t[t>tau1] - tau1))
    L2 = np.zeros_like(t)
    L2[t>tau2] = ( - 8 * b + a * (t[t>tau2] - 2 * z0 - tau2)) * (t[t>tau2] + 2 * z0 - tau2) + 8 * z0 * (2 * b + a * z0) * np.log(( - 2 * z0)/(t[t>tau2] - tau2))
                                                                                                      
    
    return   - 2 * q0 * ((c2 - 2 * b * np.pi * z0**2 - (4 * a * np.pi * z0**3)/3) * (dirac_delta(t, t + 2 * z0 - tau1) - dirac_delta(t, t + 2 * z0 - tau2)) + 1/96 * ((np.pi * (t + 2 * z0 - tau1)**2 * (16 * b * ( - t + z0 + tau1) + 3 * a * ( - t + 2 * z0 + tau1)**2) * K1)/((t - tau1)**2) - (np.pi * (t + 2 * z0 - tau2)**2 * (16 * b * ( - t + z0 + tau2) + 3 * a * ( - t + 2 * z0 + tau2)**2) * K2)/((t - tau2)**2)) + ( - c2 * t - 1/12 * b * np.pi * t**3 + 1/96 * a * np.pi * t**4 - 1/(2) * b * np.pi * t**2 * z0 + b * np.pi * t * z0**2 - 1/(4) * a * np.pi * t**2 * z0**2 - 2/3 * b * np.pi * z0**3 + 2/3 * a * np.pi * t * z0**3 - 1/(2) * a * np.pi * z0**4) * (D1 + D2 + T) + ((b * np.pi * t**2)/(4) + (a * np.pi * t * z0**2)/(2) + c2 - 1/24 * a * np.pi * t**3 + b * np.pi * t * z0 - b * np.pi * z0**2 - 2/3 * a * np.pi * z0**3) * (tau1 * D1 + tau2 * D2 + T * t) + (1/12 * b * np.pi - 1/24 * a * np.pi * t) * (tau1**3 * D1 + tau2**3 * D2 + T * (t - 4 * z0) * (t + 2 * z0)**2) + 1/96 * a * np.pi * (tau1**4 * D1 - tau2**4 * D2 + T * (t - 6 * z0) * (t + 2 * z0)**3) + ( - 1/(4) * b * np.pi * t + 1/16 * a * np.pi * t**2 - 1/(2) * b * np.pi * z0 - 1/(4) * a * np.pi * z0**2) * (tau1**2 * D1 + tau2**2 * D2 + T * (t**2 - 4 * z0**2))) + 1/(4) * q0 * np.pi * xi * (K1*L1 - K2*L2)
   
   
    
fig, ax = plt.subplots()




# for b in np.linspace(0, 100):

#     plt.plot(t, psi_pulse(t), label=f'$\\tau_2=${tau2}', color='tab:blue')


#     plt.show()


a = -1
b = -1

tau1 = 0
tau2 = 2

t = np.linspace(tau1, 10, 100000)
plt.axvline(tau1-2*z0, linestyle=':', color='black', label='$t=\\tau_1+2|z_0|$')

ax.plot(t, psi_pulse(t), label=f'b={b}', color='tab:blue')

a = -1
b = 4
ax.plot(t, psi_pulse(t), label=f'b={b}', color='tab:blue', linestyle=':')

a = -1
b = 9
ax.plot(t, psi_pulse(t), label=f'b={b}', color='tab:blue', linestyle='--')

plt.title(f'$\psi$ against time (t) for $\\tau_1=${tau1}, $\\tau_2=${tau2}, a={a}')
plt.xlabel('t')
plt.legend()
plt.show()

xx
# Monochromatic signal

def q_mono(t, omega):
    return q0 * np.sin(omega * t)

def psi_mono(t, omega):
    K1=np.heaviside(t + 2 * z0 - tau1, 1)
    Ka1=np.heaviside( - t - 2 * z0 + tau1, 1)
    K2=np.heaviside( - t - 2 * z0 + tau2, 1)
    S=np.sin((t + 2 * z0)*omega)
    C=np.cos((t + 2 * z0)*omega)
    C1=np.cos(tau1*omega)
    C2=np.cos(tau2*omega)
    D1=(dirac_delta(t, t + 2 * z0 - tau1)*np.sin(tau1*omega))/(t - tau1)
    D2=(dirac_delta(t, t + 2 * z0 - tau2)*np.sin(tau2*omega))/(t - tau2)
    T=(1)/(4*z0**2) * K1 * K2
    Ci1 = sici((-t+tau1) * omega)[1]
    Ci2 = sici((t-tau2) * omega)[1]
    Cia2 = sici((-t+tau2) * omega)[1]
    Si1 = sici((t-tau1) * omega)[0]
    Si2 = sici((t-tau2) * omega)[0]

    
    L1 = C - C1 + 2 * z0 * omega * np.sin(t * omega) * (sici(2 * z0 * omega)[1] - sici(( - t + tau1) * omega)[1]) + 2 * z0 * omega * np.cos(t * omega) * (sici(2 * z0 * omega)[0] + sici((t - tau1) * omega)[0])
    L2 = C - C2 + 2 * z0 * omega * np.sin(t * omega) * (sici(2 * z0 * omega)[1] - sici(( - t + tau2) * omega)[1]) + 2 * z0 * omega * np.cos(t * omega) * (sici(2 * z0 * omega)[0] + sici((t - tau2) * omega)[0])    
    
    return (2 * np.pi * q0 * xi * rho0)/(omega) * ( - C1 + C2 + 2 * z0 * omega * np.sin(t * omega) * ( - Ci1 + Cia2) + 2 * z0 * omega * np.cos(t * omega) * (Si1 - Si2) - Ka1 * L1 + K2 * L2) - 2 * ( - 2 * np.pi * q0 * z0**2 * rho0 * (omega * C * K1 * K2 + dirac_delta(t, t + 2 * z0 - tau1) * np.sin(tau1 * omega) - dirac_delta(t, t + 2 * z0 - tau2) * np.sin(tau2 * omega)) + np.pi * q0 * rho0 * ( - (t**3)/12 - (2 * t**2 * z0)/(2) + t * z0**2 - (2 * z0**3)/3) * (T * ( - 2 * z0 * omega * C + S) + D1 - D2) + ((t**2)/(4) + t * z0 - z0**2) * np.pi * q0 * rho0 * ( - T * (2 * z0 * (t + 2 * z0) * omega * C - t * S) + (tau1 * D1) - (tau2 * D2)) - (np.pi * q0 * rho0)/(2) * ((t)/(2) + z0) * ( - T * (t + 2 * z0) * (2 * z0 * (t + 2 * z0) * omega * C - (t - 2 * z0) * S) + (tau1**2 * D1) - (tau2**2 * D2)) + (np.pi * q0 * rho0)/12 * ( - T * (t + 2 * z0)**2 * (2 * z0 * (t + 2 * z0) * omega * C - (t - 4 * z0) * S) + (tau1**3 * D1) - (tau2**3 * D2)) + (np.pi * q0 * rho0)/(6) * ( - ((t - tau1 + 4 * z0**3 * omega**2) * C1)/((t - tau1) * omega) + ((t - tau2 + 4 * z0**3 * omega**2) * C2)/((t - tau2) * omega) + 4 * z0**3 * ((np.sin(tau1 * omega))/((t - tau1)**2) - (np.sin(tau2 * omega))/((t - tau2)**2) + omega**2 * ((Ci1 - Ci2) * np.sin(t * omega) + (Si2 - Si1) * np.cos(t * omega)))))



omega=1



fig, ax = plt.subplots()


t = np.linspace(0, 7, 100000)
tau1 = 0
tau2 = 1

plt.axvline(tau2-2*z0, linestyle=':', color='black', label='$t=\\tau_1+2|z_0|$')


ax.plot(t, psi_mono(t, omega), label=f'$\\tau_2=${tau2}', color='tab:blue')

tau1 = 0
tau2 = 2
ax.plot(t, psi_mono(t, omega), label=f'$\\tau_2=${tau2}', color='tab:blue', linestyle=':')

tau1 = 0
tau2 = 3
ax.plot(t, psi_mono(t, omega), label=f'$\\tau_2=${tau2}', color='tab:blue', linestyle='--')


plt.ylim([-100, 100])
plt.title(f'$\psi$ against time (t) for $\\tau_1=${tau1}, $\\xi=${xi}')
plt.xlabel('t')
# plt.legend()
plt.show()
