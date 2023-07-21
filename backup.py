import matplotlib.pyplot as plt
import numpy as np
from tempfile import TemporaryFile

plt.rcParams.update({'font.size': 12})

H0 = 10.
t0 = 100.
x0 = 0.
x_end = 1.
dx = 0.01

x_list = np.array([x0])
t_list = np.array([t0])
H_list = np.array([H0])

rk4tables = TemporaryFile()

x = x0
t = t0
H = H0


def RungeKuttaCoupled(x, y, z, dx, dydx, dzdx):
    k1 = dx * dydx(x, y, z)
    h1 = dx * dzdx(x, y, z)
    k2 = dx * dydx(x + dx / 2., y + k1 / 2., z + h1 / 2.)
    h2 = dx * dzdx(x + dx / 2., y + k1 / 2., z + h1 / 2.)
    k3 = dx * dydx(x + dx / 2., y + k2 / 2., z + h2 / 2.)
    h3 = dx * dzdx(x + dx / 2., y + k2 / 2., z + h2 / 2.)
    k4 = dx * dydx(x + dx, y + k3, z + h3)
    h4 = dx * dzdx(x + dx, y + k3, z + h3)

    y = y + 1. / 6. * (k1 + 2 * k2 + 2 * k3 + k4)
    z = z + 1. / 6. * (h1 + 2 * h2 + 2 * h3 + h4)
    x = x + dx

    return x, y, z


def dHdx(x, t, H):
    # dH/dx = K*(t-t_ext)
    # K = 1
    # t_ext = 0
    return t


def dtdx(x, t, H):
    return -H


while x <= x_end:
    x, t, H = RungeKuttaCoupled(x, t, H, dx, dtdx, dHdx)

    x_list = np.append(x_list, x)
    t_list = np.append(t_list, t)
    H_list = np.append(H_list, H)


np.savez(rk4tables, x=x_list, t=t_list, H=H_list)
_ = rk4tables.seek(0)
tables = np.load(rk4tables)
print(tables.files)

fig, axes = plt.subplots(1,2,figsize=(7,3))

ax1 = axes[0]
ax2 = axes[1]

ax1.plot(tables['x'], tables['t'],
        color="blue")
ax1.set_xlabel("Length")
ax1.set_ylabel("Temperature")
ax1.text(0,50,r"$\tau(1)=%.2f^\circ$C" % tables['t'][-1])

ax2.plot(tables['x'], tables['H'],
        color="magenta")
ax2.set_xlabel("Length")
ax2.set_ylabel("Heat flux")
ax2.text(0,80,r"$H(1)=%.2f$ W/m$^2$" % tables['H'][-1])

plt.subplots_adjust(wspace=0.3)

plt.show()
