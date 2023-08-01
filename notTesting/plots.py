import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.style.use('dark_background')


def show():
    with np.load('rk4tables.npz') as tables:
        fig, ax = plt.subplots(1, 1,figsize=(7,7))
        ax.plot(tables['x'], tables['y'], color="blue")
        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")

        ax.text(0.5,0.5,r"$y(2)=%.2f$" % tables['y'][-2], horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
    plt.show()
