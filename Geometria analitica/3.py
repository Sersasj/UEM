#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:31:11 2019

@author: sergio
"""


print("Este programa determina a area de um paralelogramo ABCD")
print("Voce deve entrar com 3 pontos ABC e o programa calculara a area com D oposto a B")
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
    
   
    #calcula o modulo de \ABXAC\ para achar a area do paralelogramo
    modulo1 = i**2
    modulo2 = j**2
    modulo3 = k**2
    modulo = (modulo1+modulo2+modulo3)**0.5
    print("A area do paralelogramo eh:",modulo)

    #soma BA em C para achar ponto D
    BA = [elemv1  - elemv2 for elemv1, elemv2 in zip(v2,v1)]
    pontoD = [elemv3  + elemvBA for elemv3, elemvBA in zip(v3,BA)]
    print("O ponto D eh: ",pontoD)
    
else:
    print("Erro")    
     
    