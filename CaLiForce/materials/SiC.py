from scipy.constants import c, pi

# from Palik p.588
materialclass = "dielectric"
cminv_to_radpersec = 2*pi*100*c
wL = 969*cminv_to_radpersec
wT = 793*cminv_to_radpersec
gamma = 4.76*cminv_to_radpersec
eps_inf = 6.7

def epsilon(xi):
    return eps_inf*(1 + (wL**2 - wT**2)/(wT**2 + xi**2 + gamma*xi))

