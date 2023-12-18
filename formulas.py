import numpy as np


def velocity_of_prop(u_carrier, e_bed, rho_part, dq_dc):
    """Concentration velocity of propagation"""
    return u_carrier / ((1 - e_bed) * rho_part * dq_dc)
