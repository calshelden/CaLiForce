import numpy as np
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
    res_TE = k / 2 / pi * log1p(- rTE_L * rTE_R * exp(-2 * kappa * d))
    res_TM = k / 2 / pi * log1p(- rTM_L * rTM_R * exp(-2 * kappa * d))
    return res_TE, res_TM

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
    f_TE = lambda t: k_integrand_energy(t/d, k0, d, epsm_func(k0 * c), rL, rR)[0]/d
    res_TE = quad(f_TE, 0, inf)[0]
    f_TM = lambda t: k_integrand_energy(t/d, k0, d, epsm_func(k0 * c), rL, rR)[1]/d
    res_TM = quad(f_TM, 0, inf)[0]
    return np.array([res_TE, res_TM])

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
    res_TE = -2 * k * kappa / 2 / pi * rTE_L * rTE_R * exp(-2 * kappa * d) / (1 - rTE_L * rTE_R * exp(-2 * kappa * d))
    res_TM = -2 * k * kappa / 2 / pi * rTM_L * rTM_R * exp(-2 * kappa * d) / (1 - rTM_L * rTM_R * exp(-2 * kappa * d))
    return res_TE, res_TM

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
    f_TE = lambda t: k_integrand_pressure(t / d, k0, d, epsm_func(k0 * c), rL, rR)[0] / d
    res_TE = quad(f_TE, 0, inf)[0]
    f_TM = lambda t: k_integrand_pressure(t / d, k0, d, epsm_func(k0 * c), rL, rR)[1] / d
    res_TM = quad(f_TM, 0, inf)[0]
    return np.array([res_TE, res_TM])

def k_integrand_pressuregradient(k, k0, d, epsm, rL, rR):
    kappa = sqrt(epsm * k0 ** 2 + k ** 2)
    rTM_L, rTE_L = rL(k0, k)
    rTM_R, rTE_R = rR(k0, k)
    res_TE = 4 * k * kappa ** 2 / 2 / pi * rTE_L * rTE_R * exp(-2 * kappa * d) / (1 - rTE_L * rTE_R * exp(-2 * kappa * d))**2
    res_TM = 4 * k * kappa ** 2 / 2 / pi * rTM_L * rTM_R * exp(-2 * kappa * d) / (1 - rTM_L * rTM_R * exp(-2 * kappa * d))**2
    return res_TE, res_TM

def k0_func_pressuregradient(k0, d, epsm_func, rL, rR):
    f_TE = lambda t: k_integrand_pressuregradient(t / d, k0, d, epsm_func(k0 * c), rL, rR)[0] / d
    res_TE = quad(f_TE, 0, inf)[0]
    f_TM = lambda t: k_integrand_pressuregradient(t / d, k0, d, epsm_func(k0 * c), rL, rR)[1] / d
    res_TM = quad(f_TM, 0, inf)[0]
    return np.array([res_TE, res_TM])