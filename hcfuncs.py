import numpy as np


def xyGrid(ax, ay, nx, ny):
    dx, dy = (ax / nx, ay / ny)
    x = np.linspace(-ax / 2, ax / 2 - dx, nx)
    y = np.linspace(-ay / 2, ay / 2 - dy, ny)
    xx, yy = np.meshgrid(x, y)
    return xx, yy


def planewave(lam,qx,qy,xx,yy):
    pi2 = np.pi*2
    k= pi2/lam
    EE = np.exp(1j*k*(qx*xx+qy*yy))
    return EE
