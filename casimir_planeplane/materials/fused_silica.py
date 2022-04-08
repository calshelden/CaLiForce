"""
Fused silica according to wikipedia (Sellmeier equation)

"""
import numpy as np
from scipy.constants import pi, c

B1 = 0.696166300
B2 = 0.407942600
B3 = 0.897479400
C1 = 4.67914826e-3*1.e-12
C2 = 1.35120631e-2*1.e-12
C3 = 97.9325*1.e-12

def epsilon(xi):
    l = 2*pi*c/xi
    return 1 + B1/(1+C1/l**2) + B2/(1+C2/l**2) + B3/(1+C3/l**2)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import sys
    sys.path.append("/home/benjamin/wd/nystrom/material")
    import silica

    xi = np.logspace(12, 18, 100)
    eps1 = epsilon(xi)
    eps2 = [silica.epsilon(x) for x in xi]

    plt.semilogx(xi, eps1)
    plt.semilogx(xi, eps2)
    plt.show()

