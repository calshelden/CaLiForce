"""
amorphous Al2O3 using simple Sellmeier equation. This ignores the loss and is only accurate when far from the resonances.

"""
from scipy.constants import pi, c

materialclass = "dielectric"

def epsilon(xi):
    if xi == 0.:
        return 1 + 1.024 + 1.058 + 5.28
    else:
        l = 2*pi*c/xi
        return 1 + 1.024*l**2/(l**2 + (0.0614e-6)**2) + 1.058*l**2/(l**2 + (0.111e-6)**2) + 5.28*l**2/(l**2 + (17.93e-6)**2)
