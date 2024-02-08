"""
We calculate the Casimir energy and pressure between two gold half-spaces in vacuum at 300K and separation of 1 micron.
"""
from CaLiForce.compute import system
from CaLiForce.materials import gold, vacuum

T = 300     # in K
d = 1.e-6   # in m
s = system(T, d, gold, gold, vacuum)
print('energy:  ', s.calculate('energy'))
print('pressure:', s.calculate('pressure'))


