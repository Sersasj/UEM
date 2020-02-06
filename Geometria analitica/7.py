#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:46:20 2019

@author: sergio
"""

print("Este programa calcula a area da base ,volume e altura de um paralelepidedo com vertice 0,0,0 em comum.")
print("\nDigite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vetor 2: ") + ']')
v3 = eval('[' + input("Digite as coordenas do vetor 3: ") + ']')


if len(v1) == len(v2) == len(v3):
    


    
    #calcula o produto vetorial
    i1 = v1[1]*v2[2]
    j1 = v1[2]*v2[0]
    k1 = v1[0]*v2[1]
    
    k2 = v1[1]*v2[0]*-1
    i2 = v1[2]*v2[1]*-1
    j2 = v1[0]*v2[2]*-1   
    i = i1+i2
    j = j1+j2
    k = k1+k2
    
    
    #calcula o modulo para achar a area da base
    modulo1 = i**2
    modulo2 = j**2
    modulo3 = k**2
    modulo = (modulo1+modulo2+modulo3)**0.5
    
        
    #faz produto escalar de v3*produto vetorial para achar produto misto
    produto_misto = ((v3[0]*i)+(v3[1]*j)+(v3[2]*k))
    #calcula a altura
    altura = produto_misto/modulo
    
    print("\nO volume do paralelepipedo eh",produto_misto)
    print("\nA area da base eh",modulo)
    print("\nA altura do paralelepidedo eh",altura)

else:
    print("Erro")

