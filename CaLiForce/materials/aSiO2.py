"""
amorphous SiO2 using simple Sellmeier equation. This ignores the loss and is only accurate when far from the resonances.

"""
from scipy.constants import pi, c

materialclass = "dielectric"

def epsilon(xi):
    if xi == 0.:
        return 1 + 0.696 + 0.408 + 0.897
    else:
        la = 2*pi*c/xi
        return 1 + 0.696*la**2/(la**2 + (0.0684e-6)**2) + 0.408*la**2/(la**2 + (0.116e-6)**2) + 0.897*la**2/(la**2 + (9.896e-6)**2)
