from CaLiForce.compute import system
from CaLiForce.materials import pec, vacuum
from scipy.constants import hbar, c, pi
from numpy.testing import assert_allclose

def cas_energy(d):
    # Casmir's result for energy at T=0
    return -hbar*c*pi**2/720./d**3

def cas_pressure(d):
    # Casmir's result for pressure at T=0
    return -hbar*c*pi**2/240./d**4

def cas_pressuregradient(d):
    # Casmir's result for pressure gradient at T=0
    return hbar*c*pi**2/60./d**5

def test_pec():
    # test Casimir interaction for pec-pec in vacuum against Casimir's exact results
    d = 1.e-6
    s = system(0., d, pec, pec, vacuum)
    assert_allclose(s.calculate('energy'), cas_energy(d))
    assert_allclose(s.calculate('pressure'), cas_pressure(d))
    assert_allclose(s.calculate('pressuregradient'), cas_pressuregradient(d))

def test_zero_frequency():



if __name__ == '__main__':
    test_pec()
