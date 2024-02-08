# from P.J. Zwol, G. Palasantzas, Phys. Rev. A 81, 062502 (2010)
import numpy as np
from scipy.constants import e as eV
from scipy.constants import hbar
materialclass = 'dielectric'

data = np.array([[9.57e-1, 1.62e0, 1.40e-1, 1.26e-1, 4.16e-1, 2.44e-1, 7.10e-2],
                 [1.62e-3, 4.32e-3, 1.12e-1, 6.87e0, 1.52e1, 1.56e1, 4.38e1]])

C = data[0]
wi = data[1]*eV/hbar

def epsilon(xi):
    if xi == 0.:
        return 24.3
    else:
        return 1 + np.sum(C/(1 + (xi/wi)**2))

