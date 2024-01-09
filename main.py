"""
This file contains the main script for the simulation of the adsorption and desorption process
of a gas in a porous material. This is used to calculate the production of methane from syn gas in Zeolite 3A.
The simulation is based on the Langmuir theory.
"""
import math
from enum import Enum

from matplotlib import pyplot as plt

from formulas import *

Adsorbed_H2O_0 = 0   # Amount of water in reactor at start.


if __name__ == "__main__":
    R = 8.314  # J/mol K
    
    def plot_3d(T_values, p_values, q_f):
        T_values, p_values = np.meshgrid(T_values, p_values)

        ax = fig.add_subplot(1, 3, 1, projection='3d')

        # Plot the surface
        ax.plot_surface(T_values, p_values / 10**5, q_f(T_values, p_values))

        ax.set_xlabel("T (K)")
        ax.set_ylabel("p (bar)")
        ax.set_zlabel("q_A (kg/kg)")


    def plot_2d(T_values, p_values, q_f):
        ax = fig.add_subplot(1, 3, 2)

        for _T in T_values:
            plt.plot((p_values) / (R * _T), q_f(_T, p_values), label=f"T = {_T} K")

        ax.set_xlabel("C (mol/m^3)")
        ax.set_ylabel("q (kg/kg)")

        plt.legend()


    def plot_2d_der(T_values, p_values, q_f):
        ax = fig.add_subplot(1, 3, 3)

        for _T in T_values:
            plt.plot((p_values) / (R * _T), np.gradient(q_f(_T, p_values)), label=f"T = {_T} K")

        ax.set_xlabel("C (mol/m^3)")
        ax.set_ylabel("q (kg/kg)")

        plt.legend()


    fig = plt.figure(figsize=(16, 9))

    Q_MAX = 1.4  # mol/kg (uit zelfde paper)
    E_ADS = 54 * 10 ** 3  # J/mol (schatting)
    T0 = 298.15  # K
    M_CH4 = 16.04 * 10**-3  # kg/mol

    dH0 = 46  # J/mol
    dS0 = 8.16  # J/mol K

    # uit paper: https://www.sciencedirect.com/science/article/abs/pii/S138718111400448X
    # B_A0 = 3.915 * 10 ** 5  # pa^-1

    B_A0 = 10e5  #b_A0(dH0, dS0, T0, R)
    print(B_A0)

    AMOUNT = 7

    # afhankelijk van reactor capaciteit
    T_values = np.linspace(273.15 + 200, 273.15 + 350, 7)

    p_values = np.linspace(0.1*10**5, 4.5*10**5, 100)

    def q_func(T_ADS, pA):
        _b_A = b_A(B_A0, E_ADS, R, T_ADS)
        return q_A_langmuir(Q_MAX, _b_A, pA) / Q_MAX
    
    def dq_dc(T_ADS, pA):
        return np.gradient(q_func(T_ADS, pA))

    plot_2d(T_values, p_values, q_func)
    plot_2d_der(T_values, p_values, q_func)
    plot_3d(T_values, p_values, q_func)

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    plt.show()
