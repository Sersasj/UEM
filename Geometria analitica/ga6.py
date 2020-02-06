#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:57:45 2019

@author: sergio
"""


import math

print("Este programa calcula os angulos internos de um triangulo em R3")
print("Digite as coordenas do vertice de um triangulo em R3\nsepare por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vertice 1: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vertice 2: ") + ']')
v3 = eval('[' + input("Digite as coordenas do vertice 3: ") + ']')
#calcula distancia vertices
ab = v2[0]-v1[0],v2[1]-v1[1],v2[2]-v1[2]
ac = v3[0]-v1[0],v3[1]-v1[1],v3[2]-v1[2]
ba = v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]
bc = v3[0]-v2[0],v3[1]-v2[1],v3[2]-v2[2]
cb = v2[0]-v3[0],v2[1]-v3[1],v2[2]-v3[2]
ca = v1[0]-v3[0],v1[1]-v3[1],v1[2]-v3[2]
#calcula modulo
modulo_ab = ((ab[0]**2)+(ab[1]**2)+(ab[2]**2))**0.5
modulo_ac = ((ac[0]**2)+(ac[1]**2)+(ac[2]**2))**0.5
modulo_ba = ((ba[0]**2)+(ba[1]**2)+(ba[2]**2))**0.5
modulo_bc = ((bc[0]**2)+(bc[1]**2)+(bc[2]**2))**0.5
modulo_cb = ((cb[0]**2)+(cb[1]**2)+(cb[2]**2))**0.5
modulo_ca = ((ca[0]**2)+(ca[1]**2)+(ca[2]**2))**0.5
#calcula o produto escalar
escalar_1 =((ab[0]*ac[0])+(ab[1]*ac[1])+(ab[2]*ac[2]))
escalar_2 =((ba[0]*bc[0])+(ba[1]*bc[1])+(ba[2]*bc[2]))
escalar_3 =((cb[0]*ca[0])+(cb[1]*ca[1])+(cb[2]*ca[2]))


cos1 = escalar_1/(modulo_ab*modulo_ac)
cos2 = escalar_2/(modulo_ba*modulo_bc)
cos3 = escalar_3/(modulo_cb*modulo_ac)

radiano1 =  math.acos(cos1)
print("\nO angulo em radianos de alfa é: ",radiano1)
radiano2 =  math.acos(cos2)
print("\nO angulo em radianos beta é: ",radiano2)
radiano3 =  math.acos(cos3)
print("\nO angulo em radianos gama é: ",radiano3)

graus1 = math.degrees(radiano1)
print("\nO angulo em graus de alfa é: ",graus1)
graus2 = math.degrees(radiano2)
print("\nO angulo em graus de beta é: ",graus2)
graus3 = math.degrees(radiano3)
print("\nO angulo em graus de gama é : ",graus3)
