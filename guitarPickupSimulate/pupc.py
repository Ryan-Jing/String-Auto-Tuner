from matplotlib.pyplot import *
import numpy as np
import time


# Starting and ending frequency and number of frequencies
class pupc():
    def __init__(self, fs, fe, fnum):
        self.f = np.linspace(fs, fe, num = fnum)

# Method to return impedance of a capacitor
    def fZC(self, C):
        return -1.j/(2.*np.pi*self.f*C)

# Method to return impedance of an inductor
    def fZL(self, L):
        return 1.j*2*np.pi*self.f*L

# Method to parallel 2 or more impedances
    def par(self, Zf, *Zs):
        admit = 1./Zf
        for Z in Zs:
            admit += 1./Z
        return 1./admit

# Method to find the response of a voltage divider
    def vdiv(self, Zser, Zshu):
        return Zshu/(Zser + Zshu)

# Method to make a plot of the results of vdiv
    def plres(self, res, str):
        figure()
        semilogx(self.f, 20.*np.log10(np.absolute(res)))
        grid()
        xlabel('Frequency (Hz)')
        ylabel('Response (0 = unity gain)')
        title('{0:s} {1:s}'.format(str, time.ctime()))
        show()