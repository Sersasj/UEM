#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:37:50 2019

@author: sergio
"""
#programa para calcular vetor resultante

print("Este programa calcula o produto escalar de R3.\n\nDigite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vetor 2: ") + ']')


print("O produto escalar é: ")
#calculo do produto escalar
print((v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2]))
