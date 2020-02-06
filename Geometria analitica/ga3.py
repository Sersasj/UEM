#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:51:36 2019

@author: sergio
"""

print("Este programa calcula o vetor paralelo tal que vetor1*vetor2=k")
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
u1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
k = float(input("Digite uma constante k, tal que u*v=k "))
#calcula o produto escalar
soma_u1 = u1[0]*u1[0]+u1[1]*u1[1]+u1[2]*u1[2]
#acha o "x" do produto escalar
x = k/soma_u1
#calcula x * u1 para achar v
v = u1[0]*x,u1[1]*x,u1[2]*x

print("O vetor v é: ",v)
