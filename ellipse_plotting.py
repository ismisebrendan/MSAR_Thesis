import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

fig, ax = plt.subplots()

c = 1
# Semi major axis
a = 1.4
b = np.sqrt(a**2 - c**2)

t = np.linspace(0, 2*np.pi, 1000)
ellipse_x = a * np.cos(t)
ellipse_y = b * np.sin(t)

y_intercept = ellipse_y[np.argmin(np.abs(ellipse_x + 0.5))]
theta2 = np.degrees(np.arctan2([1,0], [-0.5, y_intercept]))[0]
plt.scatter(-0.5, y_intercept, color='green', s=10)
plt.plot([-0.5, 0], [y_intercept, 0], color='green')
plt.text(-0.5, y_intercept, " $x''$", va='bottom', ha='left')

wedge = Wedge([0,0], 0.5, theta1=0, theta2=theta2, color=(0,1,0,0.5), edgecolor='green', fill=True)
ax.add_patch(wedge)
plt.text(0.1, 0.5, "$\\theta_0$")

plt.plot(ellipse_x, ellipse_y, color='black')
plt.scatter(c, 0, color='black', s=10)
plt.scatter(-c, 0, color='black', s=10)
plt.scatter(0, 0, color='black', s=10)
plt.scatter(-0.5, 0, color='red', s=10)
plt.text(c, 0, " $x$", va='bottom', ha='left')
plt.text(-c, 0, " $x'$", va='bottom', ha='left')
plt.text(0, 0, " $x_0$", va='top', ha='left')
plt.text(-0.5, 0, " $z_0$", va='top', ha='left')

plt.fill_between([-10, -0.5], -10, 10, color=(1,0,0,0.5))
plt.hlines(0, -4, 4, color='black')

plt.axis('equal')
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.show()

