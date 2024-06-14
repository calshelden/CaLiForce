materialclass = "dielectric"

def epsilon(xi):
    c1 = 7.666
    w1 = 3.685
    c2 = 2.913
    w2 = 6.354
    c3 = 0.06169
    w3 = 48.66
    return 1 + c1/(1+(xi/w1)**2) + c2/(1+(xi/w2)**2) + c3/(1+(xi/w3)**2)
