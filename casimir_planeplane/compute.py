from .plane import def_reflection_coeff
from .interaction import k0_func_energy, k0_func_pressure, k0_func_pressuregradient
from .frequency_summation import psd_sum, msd_sum
from scipy.constants import k as kB
from scipy.constants import pi, c, hbar
from scipy.integrate import quad
from math import inf

class system:
    def __init__(self, T, d, matL, matR, matm, deltaL=[], deltaR=[]):
        self.T = T
        self.d = d
        if not isinstance(matL, list):
            self.matL = [matL]
        else:
            self.matL = matL
        self.deltaL = deltaL
        if not isinstance(matR, list):
            self.matR = [matR]
        else:
            self.matR = matR
        self.deltaR = deltaR
        self.matm = matm

        if not len(self.matL) == len(self.deltaL) + 1:
            raise ValueError("A thickness needs to assigned to each coating layer on plate L, i.e. len(matL)=len(deltaL)+1 must hold.")
        if not len(self.matR) == len(self.deltaR) + 1:
            raise ValueError("A thickness needs to assigned to each coating layer on plate R, i.e. len(matR)=len(deltaR)+1 must hold.")

    def calculate(self, observable, fs='psd', epsrel=1.e-8, N=None):
        if observable == 'energy':
            func = k0_func_energy
        elif observable == 'pressure':
            func = k0_func_pressure
        elif observable == 'pressuregradient':
            func = k0_func_pressuregradient
        else:
            raise ValueError('Supported values for \'observable\' are either \'energy\', \'pressure\' or \'pressuregradient\'!')

        # define reflection coefficients
        rL = def_reflection_coeff(self.matm, self.matL, self.deltaL)
        rR = def_reflection_coeff(self.matm, self.matR, self.deltaR)

        # define frequency (wave vector) integrand/summand
        self.f = lambda k0: func(k0, self.d, self.matm.epsilon, rL, rR)

        if self.T == 0.:
            # frequency integration
            t_func = lambda t: self.f(t / self.d) / self.d
            return hbar * c / 2 / pi * quad(t_func, 0, inf)[0]
        else:
            # frequency summation
            if fs == 'psd':
                fsum = psd_sum
            elif fs == 'msd':
                fsum = msd_sum
            else:
                raise ValueError('Supported values for fs are either \'psd\' or \'msd\'!')

            self.n0 = 0.5 * self.T * kB * self.f(0.)
            self.n1 = fsum(self.T, self.d, self.f, epsrel=epsrel, order=N)
            return self.n0 + self.n1
