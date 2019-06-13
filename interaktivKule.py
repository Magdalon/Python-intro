# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:45:44 2019

@author: magopda
"""

from math import pi

def overflate(radius):
    minOverflate = 4*pi*radius**2
    return minOverflate

def volum(radius):
    mittVolum = 4/3*pi*radius**3
    return mittVolum

spørsmål = "Radius i centimeter?"
tekst = input(spørsmål)
radius = float(tekst)

utregnetOverflate = overflate(radius)
forklaringOverflate="Overflate i kvadratcentimeter:"
print(forklaringOverflate, utregnetOverflate)

utregnetVolum = volum(radius)
forklaringVolum="Volum i kubikkcentimeter:"
print(forklaringVolum, utregnetVolum)