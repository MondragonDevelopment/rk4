import numpy as np
import rk4
import plots as plt
import functions as f
from shooting import yf
from scipy.optimize import newton

y0 = 1.
x0 = 0.
x_end = 2.
V0 = newton(yf, 8)
dx = 0.02

x_list = np.array([x0])
y_list = np.array([y0])
V_list = np.array([V0])

x = x0
y = y0
V = V0


while x <= x_end:
    V = rk4.method(x, y, V, dx, f.dVdx)
    y = rk4.method(x, V, y, dx, f.dydx)
    x = x + dx

    x_list = np.append(x_list, x)
    y_list = np.append(y_list, y)
    V_list = np.append(V_list, V)



np.savez('rk4tables', x=x_list, y=y_list, V=V_list)

plt.show()
