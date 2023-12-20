"""
This file contains the main script for the simulation of the adsorption and desorption process
of a gas in a porous material. This is used to calculate the production of methane from syn gas in Zeolite 3A.
The simulation is based on the Langmuir theory.
"""
from enum import Enum
from matplotlib import pyplot as plt
import math

from formulas import *

# CONSTANTS

qmax        =       100             #Max amount adsorbed
k_ads       =       10              #adsorption constant
k_des       =       10              #desorption constant
B_a0        =       k_ads/k_des     
deltaE_ads  =       -50             #Adsorption energy- negative for a exothermic reeaction 
R           =       8.31446261      #Gas constant
T           =       623             #Temperature in Kelvin


# PARAMETERS
T_ADS = np.float32(273.15 + 250)    # Temperature during adsorption in Kelvin
P_ADS = np.float32(150 * 10 ** 5)   # Pressure during adsorption in Pascal

T_DES = np.float32(273.15 + 250)    # Temperature during desorption in Kelvin
P_DES = np.float32(1.0 * 10 ** 5)   # Pressure during desorption in Pascal


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
        self.delta_time: float = 0.1

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

    def plot_3d(x, y, z_func):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # Plot the surface
        ax.plot_surface(x, y, z_func(x,y))

        ax.set_xlabel("T (K)")
        ax.set_ylabel("p (Pa)")
        ax.set_zlabel("q_A (mol/kg)")

        plt.show()


    # uit paper: https://www.sciencedirect.com/science/article/abs/pii/S138718111400448X
    B_A0 = 3.915 * 10 ** 5  # pa^-1
    Q_MAX = 3.2 # mol/kg (uit zelfde paper)
    E_ADS = 1.2 * 10 ** 3  # J/mol (ONGEBASEERD, VOLLEDIG WILLEKEURIG GEKOZEN)
    R = 8.314  # J/mol K


    # afhankelijk van reactor capaciteit
    T_values = np.linspace(273.15 + 200, 273.15 + 350, 100)
    # in paper: https://pubs.acs.org/doi/10.1021/acs.jpcc.6b09224
    # wordt een partial pressure tussen 0 en 2kPa genoemd
    p_values = np.linspace(100, 2000, 100)

    def z_func(T_ADS, pA):
        _b_A = b_A(B_A0, E_ADS, R, T_ADS)
        return q_A_langmuir(Q_MAX, _b_A, pA)

    T_values, p_values = np.meshgrid(T_values, p_values)

    plot_3d(T_values, p_values, z_func)
