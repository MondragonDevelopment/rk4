import numpy as np
import rk4
import plots as plt

H0 = 10.
t0 = 100.
x0 = 0.
x_end = 1.
dx = 0.01

x_list = np.array([x0])
t_list = np.array([t0])
H_list = np.array([H0])

x = x0
t = t0
H = H0


while x <= x_end:
    x, t, H = rk4.method(x, t, H, dx)

    x_list = np.append(x_list, x)
    t_list = np.append(t_list, t)
    H_list = np.append(H_list, H)


np.savez('rk4tables', x=x_list, t=t_list, H=H_list)

plt.show()