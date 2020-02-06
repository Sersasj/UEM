#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:37:57 2019

@author: sergio
"""

i = 0
resultado = 0

print("Este programa calcula o produto escalar")
r = int(input("Digite a dimensao desejada: "))
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vetor 2: ") + ']')


print("O produto escalar é: ")
#calcula o produto escalar 
while i < r:
    resultado += v1[i]*v2[i]
    i +=1
print (resultado)
    
        