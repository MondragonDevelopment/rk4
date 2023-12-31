import functions as f

def method(x, t, H, dx, dtdx, dHdx):  # Runge-Kutta Coupled Method
    k1 = dx * dtdx(x, t, H)
    h1 = dx * dHdx(x, t, H)
    k2 = dx * dtdx(x + dx / 2., t + k1 / 2., H + h1 / 2.)
    h2 = dx * dHdx(x + dx / 2., t + k1 / 2., H + h1 / 2.)
    k3 = dx * dtdx(x + dx / 2., t + k2 / 2., H + h2 / 2.)
    h3 = dx * dHdx(x + dx / 2., t + k2 / 2., H + h2 / 2.)
    k4 = dx * dtdx(x + dx, t + k3, H + h3)
    h4 = dx * dHdx(x + dx, t + k3, H + h3)

    t = t + 1. / 6. * (k1 + 2 * k2 + 2 * k3 + k4)
    H = H + 1. / 6. * (h1 + 2 * h2 + 2 * h3 + h4)
    x = x + dx

    return x, t, H
