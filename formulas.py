import numpy as np


def theta_A(q_A, q_maxA):
    """
    Fraction of adsorption sites occupied by A
    :param q_A: amount of A adsorbed
    :param q_maxA: maximum adsorption capacity of A, with theta_A = 1
    :return: fraction of adsorption sites occupied by A
    """
    return q_A / q_maxA


def q_A_henry(q_maxA, b_A, p_A):
    """
    Henry's law adsorption isotherm
    :param q_maxA: maximum adsorption capacity of A
    :param b_A: adsorption constant of A
    :param p_A: partial pressure of A
    :return: amount of A adsorbed
    """
    return q_maxA * b_A * p_A


def q_A_langmuir(q_maxA, b_A, p_A):
    """
    Langmuir adsorption isotherm
    :param q_maxA: maximum adsorption capacity of A
    :param b_A: adsorption constant of A
    :param p_A: partial pressure of A
    :return: amount of A adsorbed
    """
    return q_maxA * b_A * p_A / (1 + b_A * p_A)


def b_A_from_k(k_ads, k_des):
    """
    Adsorption constant of A
    :param k_ads: adsorption rate constant (first order)
    :param k_des: desorption rate constant (zero order)
    :return: adsorption constant of A
    """
    return k_ads / k_des


def b_A(b_A0, delta_E_ads, R, T):
    """
    Adsorption constant of A
    :param b_A0: adsorption constant of A at standard conditions
    :param delta_E_ads: activation energy of adsorption of A
    :param R: ideal gas constant
    :param T: temperature relative to standard conditions?
    :return: adsorption constant of A
    """
    return b_A0 * np.exp(-delta_E_ads / (R * T))


def u_carrier(Q, A):
    """
    Superficial velocity of the carrier gas
    :param Q: volumetric flow rate of the carrier gas
    :param A: cross-sectional area of the reactor
    :return: superficial velocity of the carrier gas
    """
    return Q / A


def v_sw(u_carrier, e_bed, rho_part, dq_dc):
    """
    Shock wave velocity
    :param u_carrier: superficial velocity of the carrier gas
    :param e_bed: porosity of the bed
    :param rho_part: density of the particles
    :param dq_dc: derivative of the adsorption isotherm
    :return: shock wave velocity
    """
    return u_carrier / ((1 - e_bed) * rho_part * dq_dc)


def e_tot(v_bed, v_part):
    """
    Porosity of the bed
    :param v_bed: volume of the bed
    :param v_part: pore volume of the bed
    :return: porosity of the bed
    """
    return 1 - (v_part / v_bed)

def alpha_AB(b_A, b_B, D_a, D_b):
    """
    Kinetic selectivity
    :param b_A: adsorption constant of A
    :param b_B: adsorption constant of B
    :param D_a: diffusion coefficient of A
    :param D_b: diffusion coefficient of B
    :return:
    """

def t_sat(L, u_carrier, e_bed, rho_part, q_star, c_f):
    """
    Saturation time
    :param L: length of the bed
    :param u_carrier: superficial velocity of the carrier gas
    :param e_bed: porosity of the bed
    :param rho_part: density of the particles
    :param q_star: amount adsorbed in equilibrium with feed concentration _c_f
    :param c_f: feed concentration (time of movement of the shock wave)
    :return: saturation time
    """
    return (L / u_carrier) * (1 / (1 - e_bed)) * (rho_part / q_star) * c_f
