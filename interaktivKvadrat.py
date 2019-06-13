# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 18:17:08 2019

@author: magopda
"""

def kvadratAreal(sidelengde):
    return sidelengde**2

sidelengde = float(input("Sidelengde i centimeter?"))
print("Areal i kvadratcentimeter:",kvadratAreal(sidelengde))