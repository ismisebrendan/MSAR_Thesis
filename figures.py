import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

#
# Ellipse
#
fig, ax = plt.subplots()

c = 1
# Semi major axis
a = 1.6
b = np.sqrt(a**2 - c**2)

z0 = -1.2

t = np.linspace(0, 2*np.pi, 1000)
ellipse_x = a * np.cos(t)
ellipse_y = b * np.sin(t)

y_intercept = np.abs(ellipse_y[np.argmin(np.abs(ellipse_x + z0))])
theta2 = np.degrees(np.arctan2(y_intercept, z0))
plt.scatter(z0, y_intercept, color='green', s=10)
plt.plot([z0, 0], [y_intercept, 0], color='green')
plt.text(z0, y_intercept, " $x''$", va='bottom', ha='right')

wedge = Wedge([0,0], 0.6, theta1=0, theta2=theta2, color=(0,1,0,0.5), edgecolor='green', fill=True)
ax.add_patch(wedge)
plt.text(0.1, 0.5, "$\\theta_0$")

plt.plot(ellipse_x, ellipse_y, color='black')
plt.scatter(c, 0, color='black', s=10)
plt.scatter(-c, 0, color='black', s=10)
plt.scatter(0, 0, color='black', s=10)
plt.scatter(z0, 0, color='red', s=10)
plt.text(c, 0, " $x$", va='bottom', ha='left')
plt.text(-c, 0, " $x'$", va='bottom', ha='left')
plt.text(0, 0, " $x_0$", va='top', ha='left')
plt.text(z0, 0, " $z_0$", va='top', ha='left')

plt.fill_between([-10, z0], -10, 10, color=(1,0,0,0.5))
plt.hlines(0, -4, 4, color='black')

plt.axis('equal')
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])


# Cartesian axis
plt.arrow(1.5, -1.1, 0.5, 0, width=0.01, head_width=0.05, length_includes_head=True, color='black')
plt.arrow(1.5, -1.1, 0, 0.5, width=0.01, head_width=0.05, length_includes_head=True, color='black')

plt.text(1.55, -0.6, '$y$')
plt.text(2, -1.05, '$z$')


plt.xticks([])
plt.yticks([])
# plt.savefig('ellipse.png', dpi=200)
plt.show()

sdffsdfd
#
# Blank ellipse
#

fig, ax = plt.subplots()

c = 1
# Semi major axis
a = 1.4
b = np.sqrt(a**2 - c**2)

# Find x''

t = np.linspace(0, 2*np.pi, 1000)
ellipse_y = a * np.cos(t)
ellipse_x = b * np.sin(t)

intercept_x = 0.8
ellipse_intercept = np.abs(ellipse_y[np.argmin(np.abs(ellipse_x-intercept_x))])

plt.scatter(intercept_x, ellipse_intercept, color='black', s=10)

plt.plot(ellipse_x, ellipse_y, color='black')
plt.scatter(0, c, color='black', s=10)
plt.scatter(0, -c, color='black', s=10)
plt.scatter(0, 0, color='black', s=10)
plt.text(0, c, " $x$", va='bottom', ha='left')
plt.text(0, -c, " $x'$", va='bottom', ha='left')
plt.text(0, 0, " $x_0$", va='top', ha='left')
plt.text(intercept_x, ellipse_intercept, " $x''$", va='bottom', ha='left')

plt.arrow(0, 0, intercept_x, ellipse_intercept, color='black', width=0.01, head_width=0.05, length_includes_head=True)

# Cartesian axis
plt.arrow(-1.7, -1.1, 0.3, 0, width=0.01, head_width=0.05, length_includes_head=True, color='black')
plt.arrow(-1.7, -1.1, 0, 0.3, width=0.01, head_width=0.05, length_includes_head=True, color='black')
plt.arrow(-1.7, -1.1, -np.sqrt(3)/10, -np.sqrt(3)/10, width=0.01, head_width=0.05, length_includes_head=True, color='black')

plt.text(-1.4, -1.1, '$y$')
plt.text(-1.7, -0.8, '$z$')
plt.text(-1.7, -1.3, '$x$')

# Ellipsoidal axis
ellipsoidal_origin = [1.5, 0.0]
plt.arrow(ellipsoidal_origin[0], ellipsoidal_origin[1], 0.4, 0, width=0.01, head_width=0.01, length_includes_head=False, color='black')
plt.arrow(ellipsoidal_origin[0], ellipsoidal_origin[1], 0, 0.4, width=0.01, head_width=0.01, length_includes_head=False, color='black')
plt.arrow(ellipsoidal_origin[0], ellipsoidal_origin[1], -0.2, -0.2, width=0.01, head_width=0.01, length_includes_head=False, color='black')

plt.arrow(ellipsoidal_origin[0], ellipsoidal_origin[1], 0.45, 0.6, head_width=0.05, length_includes_head=True, color='black')
plt.vlines(1.95, 0.6, -0.5, color='black', linestyle=':')
plt.plot([ellipsoidal_origin[0], 1.95], [ellipsoidal_origin[1], -0.5], color='black', linestyle=':')


arc_x = 0.2 * np.cos(t)
arc_y = 0.2 * np.sin(t)
theta_arc_lims = [150, 250]
phi_arc_lims = [625, 870]


plt.plot(arc_x[theta_arc_lims[0]:theta_arc_lims[1]] + ellipsoidal_origin[0], arc_y[theta_arc_lims[0]:theta_arc_lims[1]] + ellipsoidal_origin[1], color='black')

plt.plot(arc_x[phi_arc_lims[0]:phi_arc_lims[1]] + ellipsoidal_origin[0], arc_y[phi_arc_lims[0]:phi_arc_lims[1]] + ellipsoidal_origin[1], color='black')


plt.text(1.8, 0.6, '$s$')
plt.text(1.5, -0.32, '$\phi$')
plt.text(1.55, 0.25, '$\\theta$')


plt.axvline(0, color='black', linestyle=':')

plt.axis('equal')
plt.xlim([-1.5, 1.5])
ax.set_axis_off()
# plt.savefig('ellipsoidal_coords.png', dpi=200)
plt.show()






#
# Light cone
#
fig, ax = plt.subplots()
plt.plot([-2, 0, 2], [2, 0, 2], color='black')
plt.scatter(0, 0, color='red', zorder=2.5)
plt.text(0, 0, " $x'$", va='top', ha='left')
plt.axis('equal')
plt.axvline(1.1, color='black', linestyle=':')

plt.text(0.98, 0.05, 'World line\nof observer', ha='right')

plt.ylim([-0.2, 1.8])
plt.xlim([-1.5, 1.5])

ax.set_axis_off()

plt.scatter(1.1, 1.1, color='blue', zorder=2.5)
# plt.grid()
plt.savefig('light_cone.png')
plt.show()

#
# Scattering
#
fig, ax = plt.subplots()
plt.plot([-2, 0, 2], [2, 0, 2], color='black')
plt.scatter(0, 0, color='red', zorder=2.5)
plt.text(0, 0, " $x'$", va='top', ha='left')
plt.axis('equal')
plt.arrow(0, 0, -1.4, 1.4, color='purple', width=0.01, head_width=0.05, length_includes_head=True, zorder=2.4)
plt.arrow(0, 0, 0.5, 0.5, color='red', width=0.01, length_includes_head=True, zorder=2.5)
plt.arrow(0.5, 0.5, -0.4, 0.4, color='red', width=0.01, length_includes_head=True, zorder=2.5)
plt.arrow(0.1, 0.9, 0.3, 0.3, color='red', width=0.01, length_includes_head=True, zorder=2.5)
plt.arrow(0.4, 1.2, -0.2, 0.2, color='red', width=0.0001, length_includes_head=True, zorder=2.5, linestyle=':')
plt.arrow(0.2, 1.4, 0.2, 0.2, color='red', width=0.0001, length_includes_head=True, zorder=2.5, linestyle=':')

plt.ylim([-0.2, 1.8])
plt.xlim([-1.5, 1.5])
ax.set_axis_off()

# plt.grid()
plt.savefig('scattering.png')

plt.show()

#
# Light cone and scattering together
#

fig, ax = plt.subplots(1,2, figsize=[10, 3.1])

ax[0,].plot([-2, 0, 2], [2, 0, 2], color='black')
ax[0].scatter(0, 0, color='red', zorder=2.5)
ax[0].text(0, 0, " $x'$", va='top', ha='left')
ax[0].axis('equal')
ax[0].axvline(1.1, color='black', linestyle=':')
ax[0].scatter(1.1, 1.1, color='blue', zorder=2.5)
ax[0].text(0.98, 0.05, 'World line\nof observer', ha='right')

ax[0].set_ylim([-0.2, 1.8])
ax[0].set_xlim([-1.5, 1.5])
ax[0].set_xticks([])
ax[0].set_yticks([])

ax[0].text(-1.6, -0.15, 'A', fontsize=15)


ax[1].plot([-2, 0, 2], [2, 0, 2], color='black')
ax[1].scatter(0, 0, color='red', zorder=2.5)
ax[1].text(0, 0, " $x'$", va='top', ha='left')
ax[1].axis('equal')
ax[1].arrow(0, 0, -1.4, 1.4, color='purple', width=0.01, head_width=0.05, length_includes_head=True, zorder=2.4)
ax[1].arrow(0, 0, 0.5, 0.5, color='red', width=0.01, length_includes_head=True, zorder=2.5)
ax[1].arrow(0.5, 0.5, -0.4, 0.4, color='red', width=0.01, length_includes_head=True, zorder=2.5)
ax[1].arrow(0.1, 0.9, 0.3, 0.3, color='red', width=0.01, length_includes_head=True, zorder=2.5)
ax[1].arrow(0.4, 1.2, -0.2, 0.2, color='red', width=0.0001, length_includes_head=True, zorder=2.5, linestyle=':')
ax[1].arrow(0.2, 1.4, 0.2, 0.2, color='red', width=0.0001, length_includes_head=True, zorder=2.5, linestyle=':')

ax[1].set_xlim([-1.5, 1.5])
ax[1].set_ylim([-0.2, 1.8])
ax[1].set_xticks([])
ax[1].set_yticks([])

ax[1].text(-1.6, -0.15, 'B', fontsize=15)

#
# Ellipse - point particle
#
fig, ax = plt.subplots()

c = 1
# Semi major axis
a = 1.6
b = np.sqrt(a**2 - c**2)

z0 = -1.2

t = np.linspace(0, 2*np.pi, 1000)
ellipse_x = a * np.cos(t)
ellipse_y = b * np.sin(t)



plt.plot(ellipse_x, ellipse_y, color='black')
plt.scatter(c, 0, color='black', s=10)
plt.scatter(-c, 0, color='black', s=10)
plt.scatter(0.2, 0.8, color='black', s=10)
plt.text(c, 0, " $x$", va='bottom', ha='left')
plt.text(-c, 0, " $x'$", va='bottom', ha='left')
plt.text(0.2, 0.8, "$\\tilde{x}$", va='bottom', ha='left')


plt.axis('equal')
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])



plt.xticks([])
plt.yticks([])
# plt.savefig('ellipse_pp.png', dpi=200)
plt.show()


fig.tight_layout()

fig.savefig('cone_scattering.png')
