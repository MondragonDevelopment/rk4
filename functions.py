import numpy as np

def dHdx(x, t, H):
    # dH/dx = K*(t-t_ext)
    # K = 1
    # t_ext = 0
    return t


def dtdx(x, t, H):
    return -H
