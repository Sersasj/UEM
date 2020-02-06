#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:07:16 2019

@author: sergio
"""

import math

print("Este programa calcula o angulo entre dois vetores em em R3")
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vetor 2: ") + ']')


#calcula o modulo
u1 = ((v1[0]**2)+(v1[1]**2)+(v1[2]**2))**0.5
u2 = ((v2[0]**2)+(v2[1]**2)+(v2[2]**2))**0.5


#calcula o produto escalar
escalar =((v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2]))

#calcula o cosseno
cos = escalar/(u1*u2)
print ("\nO cosseno é: ",cos)
#calcula o angulo em radianos
radiano =  math.acos(cos)
print("\nO angulo em radianos é: ",radiano)

#tranforma o radiano em graus
graus = math.degrees(radiano)
print("\nO angulo em graus é: ",graus)
