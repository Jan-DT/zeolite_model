"""
This file contains the main script for the simulation of the adsorption and desorption process
of a gas in a porous material. This is used to calculate the production of methane from syn gas in Zeolite 3A.
The simulation is based on the Langmuir theory.
"""
from enum import Enum
from matplotlib import pyplot as plt

from formulas import *

# CONSTANTS

# PARAMETERS
T_ADS = np.float32(273.15 + 250)  # Temperature during adsorption in Kelvin
P_ADS = np.float32(150 * 10 ** 5)  # Pressure during adsorption in Pascal

T_DES = np.float32(273.15 + 250)  # Temperature during desorption in Kelvin
P_DES = np.float32(1.0 * 10 ** 5)  # Pressure during desorption in Pascal


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
                self.adsorption_step(self.delta_time)
            elif self.state == Reactor.State.DESORPTION:
                self.desorption_step(self.delta_time)
            else:
                raise Exception("Invalid state")

            self.time += self.delta_time

    def adsorption_step(self, dt: float):
        print("adsorption step")

    def desorption_step(self, dt: float):
        print("desorption step")

    def switch_state(self):
        if self.state == Reactor.State.ADSORPTION:
            self.state = Reactor.State.DESORPTION
        elif self.state == Reactor.State.DESORPTION:
            self.state = Reactor.State.ADSORPTION
        else:
            raise Exception("Invalid state")


if __name__ == "__main__":
    while True:
        reactor = Reactor(delta_time=0.1,
                          t_ads=T_ADS,
                          p_ads=P_ADS,
                          t_des=T_DES,
                          p_des=P_DES)

        reactor.run(duration=100)
