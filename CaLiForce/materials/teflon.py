import numpy as np
from scipy.constants import e as eV
from scipy.constants import hbar

materialclass = 'dielectric'

data = np.array([[9.30e-3, 1.83e-2, 1.39e-1, 1.12e-1, 1.95e-1, 4.38e-1, 1.06e-1, 3.86e-2],
                 [3.00e-4, 7.60e-3, 5.57e-2, 1.26e-1, 6.71e0, 1.86e1, 4.21e1, 7.76e1]])

C = data[0]
wi = data[1]*eV/hbar

# from Zwol/Palasantzas
def epsilon(xi):
    return 1 + np.sum(C/(1 + (xi/wi)**2))
"""
### THERE ARE PROBLEMS WITH C1/C2 NOT CARRYING A UNIT ###

# AF1300 according to table 2 and Eq. (4)
# in https://doi.org/10.1117/1.2965541
def epsilon(xi):
    lmbda = 2*pi*c/xi 
    #A = 1.517
    #B1 = 0.184
    #C1 = 0.016
    #B2 = 1
    #C2 = 104.66
    #A = 1.461
    #B1 = 0.226
    #C1 = 0.014
    #B2 = 1
    #C2 = 119.03
    A = 1.461
    B1 = 0.226
    C1 = 0.014e18
    B2 = 1
    C2 = 119.03e18
    return A + B1*lmbda**2/(lmbda**2 + C1) + B2*lmbda**2/(lmbda**2 + C2)
"""
