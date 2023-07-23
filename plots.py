import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.style.use('dark_background')

with np.load('rk4tables.npz') as tables:

    fig, axes = plt.subplots(1,2,figsize=(7,3))

    ax1 = axes[0]
    ax2 = axes[1]

    ax1.plot(tables['x'], tables['t'], color="blue")
    ax1.set_xlabel("Length")
    ax1.set_ylabel("Temperature")
    ax1.text(0,50,r"$\tau(1)=%.2f^\circ$C" % tables['t'][-1])

    ax2.plot(tables['x'], tables['H'],
            color="magenta")
    ax2.set_xlabel("Length")
    ax2.set_ylabel("Heat flux")
    ax2.text(0,80,r"$H(1)=%.2f$ W/m$^2$" % tables['H'][-1])

    plt.subplots_adjust(wspace=0.3)

    def show():
        plt.show()


