#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:34:57 2019

@author: sergio
"""

import math

print("Este programa calcula os angulos diretores e o modulo de um vetor")
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
#calcula o modulo
modulo = ((v1[0]**2)+(v1[1]**2)+(v1[2]**2))**0.5
#calcula o cosseno
cos1 = (v1[0]/modulo)
cos2 = (v1[1]/modulo)
cos3 = (v1[2]/modulo)

#tranforma o cosseno em radiano
radiano1 =  math.acos(cos1)
radiano2=  math.acos(cos2)
radiano3 =  math.acos(cos3)
#tranforma o radiano em graus
graus1 = math.degrees(radiano1)
graus2 = math.degrees(radiano2)
graus3 = math.degrees(radiano3)


print("\nO angulo do cos alfa em radianos é",radiano1)
print("\nO angulo do cos beta em radianos é",radiano2)
print("\nO angulo do cos gama em radianos é",radiano3)

print("\nO angulo do cos alfa em graus é: ",graus1)
print("\nO angulo do cos beta em graus é: ",graus2)
print("\nO angulo do cos gama graus é: ",graus3)

print("\nO modulo deste vetor é: ",modulo)
