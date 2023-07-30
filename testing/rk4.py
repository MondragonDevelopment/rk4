# import functions as f

def method(x, y, z, dx, dydx):  # Runge-Kutta Coupled Method
    k1 = dx * dydx(x, y)
    k2 = dx * dydx(x + dx / 2., y + k1 / 2.)
    k3 = dx * dydx(x + dx / 2., y + k2 / 2.)
    k4 = dx * dydx(x + dx, y + k3)

    z = z + 1. / 6. * (k1 + 2 * k2 + 2 * k3 + k4)
    x = x + dx

    return x, z
