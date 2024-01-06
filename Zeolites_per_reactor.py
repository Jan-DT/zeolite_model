# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 00:26:28 2023

@author: noud2
"""


import numpy as np
kg_totaal       =       50000      #Kg methaan/jaar
H2O_per_zeolite =       0.1         #Kg water die één kg zeoliet per cyclus kan opnemen.
cyclustijd      =       1          #cyclustijd in uren
n_reactors      =       2           #Aantal reactoren


kmol_methaan = kg_totaal/16.04
kmol_water      = 2 * kmol_methaan
kmol_CO2        = kmol_methaan
kmol_H2         = 4 * kmol_methaan  
liter_water = 18.016 * kmol_water

literH2O_reactorcyclus = liter_water / (n_reactors * 365 * 24/cyclustijd)
Zeoliet_per_reactor    = literH2O_reactorcyclus / H2O_per_zeolite

grondstoffen_tot = np.array([kmol_CO2, kmol_H2])
grondstoffen_s = grondstoffen_tot / (365 * 24 * 3600) 

print("Liter zeoliet per reactor:")
print( Zeoliet_per_reactor)

print("Liter water per reactor per cyclus:")
print( literH2O_reactorcyclus)
print("\n")
print("   CO2/s:          H2/s")
print(grondstoffen_s)
