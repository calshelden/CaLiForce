"""
We caculate the Casimir pressure between two gold halfspaces with a 10 nm coating on one side (where the dielectric function is specified by the user) in ethanol at 300K and separation of 1 micron.
"""
import sys
sys.path.append('..')
from casimir_planeplane.compute import system
from casimir_planeplane.materials import gold, ethanol

class user_material:
    def __init__(self):
        self.materialclass = "dielectric"
    def epsilon(self, xi):
        wj = 1.911e16  # 12.6 eV/hbar
        cj = 1.282
        return 1. + cj * wj ** 2 / (wj ** 2 + xi ** 2)

T = 300     # in K
d = 1.e-6   # in m
u = user_material()
s = system(T, d, gold, [u, gold], ethanol, deltaR=[10.e-9])
print(s.calculate('pressure'))


