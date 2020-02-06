#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:00:50 2019

@author: sergio
"""

print("Este programa calcula o volume de um tetraedro")
print("\nDigite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vertice A: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vertice B: ") + ']')
v3 = eval('[' + input("Digite as coordenas do vertice C: ") + ']')
v4 = eval('[' + input("Digite as coordenas do vertice D: ") + ']')


if len(v1) == len(v2) == len(v3):
    AB = [elemv2  - elemv1 for elemv2, elemv1 in zip(v2,v1)]    
    AC = [elemv3  - elemv1 for elemv3, elemv1 in zip(v3,v1)] 
    AD = [elemv4  - elemv1 for elemv4, elemv1 in zip(v4,v1)]

    
    #calcula o produto vetorial
    i1 = AC[1]*AD[2]
    j1 = AC[2]*AD[0]
    k1 = AC[0]*AD[1]
    
    k2 = AC[1]*AD[0]*-1
    i2 = AC[2]*AD[1]*-1
    j2 = AC[0]*AD[2]*-1 
    
    i = i1+i2
    j = j1+j2
    k = k1+k2
    
  
    
        
    #faz produto escalar de v3*produto vetorial para achar produto misto
    produto_misto = ((AB[0]*i)+(AB[1]*j)+(AB[2]*k))
    
    #divide por 6 para achar o volume do tetraedro
    volume = produto_misto/6
    print("O volume do tetraedro eh: ",volume)
else:
    print("Erro")
    