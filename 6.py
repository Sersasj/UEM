#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:37:20 2019

@author: sergio
"""


print("Este programa verifica a coplarannidade de tres vetores posição em R3.")
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
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
    #acha o produto vetorial
    resposta = i+j+k
    
        
    #faz produto escalar de v3*produto vetorial para achar produto misto
    produto_misto = ((v3[0]*i)+(v3[1]*j)+(v3[2]*k))
    #testa se os vetores sao coplanares
    if produto_misto == 0:
        print("eh coplanar")
    else:
        print("não eh coplanar")

else:
    print("Erro")