# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:27:00 2019

@author: magopda
"""

from math import pi

def omkrets(radius):
    minOmkrets = 2*pi*radius
    return minOmkrets

def areal(radius):
	mittAreal = pi*radius**2
	return mittAreal

spørsmål = "Radius i centimeter?"
tekst = input(spørsmål)
radius = float(tekst)

utregnetOmkrets = omkrets(radius)
forklaring="Omkrets i centimeter:"
print(forklaring, utregnetOmkrets)

utregnetAreal = areal(radius)
forklaringAreal="Areal i kvadratcentimeter:"
print(forklaringAreal, utregnetAreal)