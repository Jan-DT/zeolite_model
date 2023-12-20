import numpy as np


def velocity_of_prop(u_carrier, e_bed, rho_part, dq_dc):
    """Concentration velocity of propagation"""
    return u_carrier / ((1 - e_bed) * rho_part * dq_dc)


def shockwave_velocity(u_carrier, e_bed, rho_part, dq_dc):
    """Shock wave velocity"""
    return u_carrier / ((1 - e_bed) * rho_part * dq_dc)


def porosity(v_bed, v_part):
    """Porosity of the bed"""
    return 1 - (v_part / v_bed)

def u_carrier(Q, A):
    """superficial fluid velocity"""
    return Q/A

def B_a(B_a0,deltaE_ads, R, T):
    """Constant of Adsorption"""
    return B_a0 * math.e ** (deltaE_ads/ (R*T))

