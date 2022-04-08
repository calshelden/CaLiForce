from scipy.integrate import quad
from math import sqrt, exp, inf, log1p, pi
from scipy.constants import c

def k_integrand_energy(k, k0, d, epsm, rL, rR):
    """
    Integrand of the radial part of in-plane wave vector for the Casimir energy.

    :param k: in-plane wave vector
    :param k0: vacuum wave number
    :param d: separation between the two plates
    :param epsm: dielectric function of the medium evaluated at the vacuum wave number
    :param rL: reflection coefficient of the left plate
    :param rR: reflection coefficient of the right plate
    :return: float
    """
    kappa = sqrt(epsm * k0 ** 2 + k ** 2)
    rTM_L, rTE_L = rL(k0, k)
    rTM_R, rTE_R = rR(k0, k)
    resTE = log1p(- rTE_L * rTE_R * exp(-2 * kappa * d))
    resTM = log1p(- rTM_L * rTM_R * exp(-2 * kappa * d))
    return k / 2 / pi * (resTE + resTM)

def k0_func_energy(k0, d, epsm_func, rL, rR):
    """
    Casimir free energy contribution at a given wave number k0.

    :param k0: vacuum wave number
    :param d: separation between the two plates
    :param epsm_func: dielectric function of the medium
    :param rL: reflection coefficient of the left plate
    :param rR: reflection coefficient of the right plate
    :return:
    """
    f = lambda k: k_integrand_energy(k/d, k0, d, epsm_func(k0 * c), rL, rR)/d
    return quad(f, 0, inf)[0]

def k_integrand_pressure(k, k0, d, epsm, rL, rR):
    """
    Integrand of the radial part of in-plane wave vector for the Casimir pressure.

    :param k: in-plane wave vector
    :param k0: vacuum wave number
    :param d: separation between the two plates
    :param epsm: dielectric function of the medium evaluated at the vacuum wave number
    :param rL: reflection coefficient of the left plate
    :param rR: reflection coefficient of the right plate
    :return: float
    """
    kappa = sqrt(epsm * k0 ** 2 + k ** 2)
    rTM_L, rTE_L = rL(k0, k)
    rTM_R, rTE_R = rR(k0, k)
    resTE = rTE_L * rTE_R * exp(-2 * kappa * d) / (1 - rTE_L * rTE_R * exp(-2 * kappa * d))
    resTM = rTM_L * rTM_R * exp(-2 * kappa * d) / (1 - rTM_L * rTM_R * exp(-2 * kappa * d))
    return -2 * k * kappa / 2 / pi * (resTE + resTM)

def k0_func_pressure(k0, d, epsm_func, rL, rR):
    """
    Casimir pressure contribution at a given wave number k0.

    :param k0: vacuum wave number
    :param d: separation between the two plates
    :param epsm_func: dielectric function of the medium
    :param rL: reflection coefficient of the left plate
    :param rR: reflection coefficient of the right plate
    :return:
    """
    f = lambda k: k_integrand_pressure(k / d, k0, d, epsm_func(k0 * c), rL, rR) / d
    return quad(f, 0, inf)[0]

"""
# this is perhaps not relevant at this point
def k_integrand_forcegradient(k, k0, d, epsm, rL, rR):
    kappa = sqrt(epsm * k0 ** 2 + k ** 2)
    rTM_L, rTE_L = rL(k0, k)
    rTM_R, rTE_R = rR(k0, k)
    resTE = rTE_L * rTE_R * exp(-2 * kappa * d) / (1 - rTE_L * rTE_R * exp(-2 * kappa * d))**2
    resTM = rTM_L * rTM_R * exp(-2 * kappa * d) / (1 - rTM_L * rTM_R * exp(-2 * kappa * d))**2
    return 4 * k * kappa ** 2 / 2 / pi * (resTE + resTM)

def k0_func_forcegradient(k0, d, epsm_func, rL, rR):
    f = lambda k: k_integrand_energy(k / d, k0, d, epsm_func(k0 * c), rL, rR) / d
    return quad(f, 0, inf)[0]
"""