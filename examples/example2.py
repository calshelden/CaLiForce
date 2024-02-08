"""
We caculate the Casimir pressure between two gold halfspaces with a 10 nm coating on one side (where the dielectric function is specified by the user) in ethanol at 300K and separation of 1 micron.
"""
from CaLiForce.compute import system
from CaLiForce.materials import gold, ethanol

class user_material:
    def __init__(self):
        self.materialclass = "dielectric"
    def epsilon(self, xi):
        wj = 1.911e15  # 1.26 eV/hbar
        cj = 1.282
        return 1. + cj * wj ** 2 / (wj ** 2 + xi ** 2)

u = user_material()

T = 300     # in K
d = 100.e-9   # in m
s = system(T, d, gold, u, ethanol)
print(s.calculate('pressure'))


