#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:26:22 2019

@author: sergio
"""

import numpy


print("Este programa permite que voce entre com 3 pontos e ele retornara um ponto D\ntal que AB*AC=AD.")
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do ponto A: ") + ']')
v2 = eval('[' + input("Digite as coordenas do ponto B: ") + ']')
v3 = eval('[' + input("Digite as coordenas do ponto C: ") + ']')

#verifica se o tamanho sao iguais
if len(v1) == len(v2) == len(v3):
    
    #zip calcula direto v2-v1 sem precisar fazer v2[0]-v1[0]...
    AB = [elemv2  - elemv1 for elemv2, elemv1 in zip(v2,v1)]    
    AC = [elemv3  - elemv1 for elemv3, elemv1 in zip(v3,v1)]    
    
    #calcula o produto vetorial
    i1 = AB[1]*AC[2]
    j1 = AB[2]*AC[0]
    k1 = AB[0]*AC[1]
    
    k2 = AB[1]*AC[0]*-1
    i2 = AB[2]*AC[1]*-1
    j2 = AB[0]*AC[2]*-1
    
    
    i = i1+i2
    j = j1+j2
    k = k1+k2
    
    #calcula d+a para achar o ponto D
    AD1 = (i+v1[0])
    AD2 = (j+v1[1])
    AD3 = (k+v1[2])
    print("O ponto D eh: ",AD1,AD2,AD3)
    print("O vetor AD eh:",i,j,k)    

else:
    print("Erro")
    
  