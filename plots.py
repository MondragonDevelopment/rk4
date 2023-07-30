import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.style.use('dark_background')

def show():
    with np.load('rk4tables.npz') as tables:

        fig, axes = plt.subplots(1,2,figsize=(7,3))

        ax1 = axes[0]
        ax2 = axes[1]

        ax1.plot(tables['x'], tables['t'], color="blue")
        ax1.set_xlabel("$x$")
        ax1.set_ylabel("$y$")

        ax1.text(0.5, 0.5, r"$y(2)=%.2f$" % tables['t'][-1], horizontalalignment='center',
                verticalalignment='center', transform=ax1.transAxes)

        ax2.plot(tables['x'], tables['H'],
                color="magenta")
        ax2.set_xlabel("$x$")
        ax2.set_ylabel("$V$")

        ax2.text(0.5, 0.5, r"$y(2)=%.2f$" % tables['H'][-1], horizontalalignment='center',
                verticalalignment='center', transform=ax2.transAxes)

        plt.subplots_adjust(wspace=0.3)

        plt.show()


