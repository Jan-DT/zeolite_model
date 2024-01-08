"""
This file contains the main script for the simulation of the adsorption and desorption process
of a gas in a porous material. This is used to calculate the production of methane from syn gas in Zeolite 3A.
The simulation is based on the Langmuir theory.
"""
import math
from enum import Enum

from matplotlib import pyplot as plt

from formulas import *

# CONSTANTS

qmax = 100  # Max amount adsorbed
k_ads = 10  # adsorption constant
k_des = 10  # desorption constant
B_a0 = k_ads / k_des
deltaE_ads = -50  # Adsorption energy- negative for a exothermic reeaction
R = 8.31446261  # Gas constant
T = 623  # Temperature in Kelvin
M_H2 =   2.015          #Molair mass hydrogen   g/mole
M_H2O =  18.01528       #Molair mass water      g/mole
M_CH4 =  16.04          #Molair mass methane    g/mole


# PARAMETERS
T_ADS = np.float32(273.15 + 250)  # Temperature during adsorption in Kelvin
P_ADS = np.float32(150 * 10 ** 5)  # Pressure during adsorption in Pascal

T_DES = np.float32(273.15 + 250)  # Temperature during desorption in Kelvin
P_DES = np.float32(1.0 * 10 ** 5)  # Pressure during desorption in Pascal

H2_in  = np.float(1 * 10**-4)    # CO2 feed in kMole/s


# preconditions
Adsorbed_H2O_0 = 0   # Amount of water in reactor at start.


class Reactor:
    class State(Enum):
        ADSORPTION = 0
        DESORPTION = 1

    def __init__(self,
                 delta_time: float = 0.1,
                 t_ads: np.float32 = T_ADS,
                 p_ads: np.float32 = P_ADS,
                 t_des: np.float32 = T_DES,
                 p_des: np.float32 = P_DES):
        self.state: Reactor.State = Reactor.State.ADSORPTION
        self.time: float = 0.0
        self.delta_time: float = delta_time
        
        self.t_ads = t_ads
        self.p_ads = p_ads
        self.t_des = t_des
        self.p_des = p_des

    def run(self, duration: float):
        """
        Run the simulation
        :param duration: duration of the simulation in seconds
        :return:
        """
        while self.time < duration:
            if self.state == Reactor.State.ADSORPTION:
                self._adsorption_step(self.delta_time)
            elif self.state == Reactor.State.DESORPTION:
                self._desorption_step(self.delta_time)
            else:
                raise Exception("Invalid state")

            self.time += self.delta_time

    def _adsorption_step(self, dt: float):
        """
        Perform one adsorption step
        :param dt: delta time in seconds
        :return:
        """
        print("adsorption step")
        
        d_H2O_ads  =  .5 * H2_in * dt * M_H2O   # Calc the amount of water and methane formed
        d_CH4_out  =  2 * H2_in * dt * M_CH4
        
        H2O_ads = H2O_ads + d_H2O_ads           # Calc the amount of water present in the reactor
        if H2O_ads >=  qmax:
            _switch_state(self)
        

    def _desorption_step(self, dt: float):
        print("desorption step")

    def _switch_state(self):
        if self.state == Reactor.State.ADSORPTION:
            self.state = Reactor.State.DESORPTION
        elif self.state == Reactor.State.DESORPTION:
            self.state = Reactor.State.ADSORPTION
        else:
            raise Exception("Invalid state")


if __name__ == "__main__":
    # while True:
    #     reactor = Reactor(delta_time=0.1,
    #                       t_ads=T_ADS,
    #                       p_ads=P_ADS,
    #                       t_des=T_DES,
    #                       p_des=P_DES)
    #
    #     reactor.run(duration=100)

    def plot_3d(T_values, p_values, q_A_langmuir):
        T_values, p_values = np.meshgrid(T_values, p_values)

        ax = fig.add_subplot(1, 2, 1, projection='3d')

        # Plot the surface
        ax.plot_surface(T_values, p_values / 10**5, q_func(T_values, p_values))

        ax.set_xlabel("T (K)")
        ax.set_ylabel("p (bar)")
        ax.set_zlabel("q_A (kg/kg)")


    def plot_2d(T_values, p_values, q_A_langmuir):
        ax = fig.add_subplot(1, 2, 2)

        for _T in T_values:
            plt.plot(p_values / 10**5, q_func(_T, p_values), label=f"T = {_T} K")

        ax.set_xlabel("p (bar)")
        ax.set_ylabel("q (kg/kg)")

        plt.legend()


    fig = plt.figure(figsize=(16, 9))

    Q_MAX = 1.4  # mol/kg (uit zelfde paper)
    E_ADS = 54 * 10 ** 3  # J/mol (schatting)
    R = 8.314  # J/mol K
    T0 = 298.15  # K
    M_CH4 = 16.04 * 10**-3  # kg/mol

    dH0 = 46  # J/mol
    dS0 = 8.16  # J/mol K

    # uit paper: https://www.sciencedirect.com/science/article/abs/pii/S138718111400448X
    # B_A0 = 3.915 * 10 ** 5  # pa^-1

    B_A0 = 100  #b_A0(dH0, dS0, T0, R)
    print(B_A0)

    AMOUNT = 7

    # afhankelijk van reactor capaciteit
    T_values = np.linspace(273.15 + 200, 273.15 + 350, 7)

    p_values = np.linspace(0.1*10**5, 4.5*10**5, 100)


    def q_func(T_ADS, pA):
        _b_A = b_A(B_A0, E_ADS, R, T_ADS)
        return q_A_langmuir(Q_MAX, _b_A, pA) / Q_MAX

    plot_2d(T_values, p_values, q_func)
    plot_3d(T_values, p_values, q_func)

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    plt.show()
