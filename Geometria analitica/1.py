#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:37:19 2019

@author: sergio
"""
import numpy


print("Este programa calcula o produto vetorial em R3.")
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vetor 2: ") + ']')


if len(v1) == len(v2):
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
    
    
    print("Resultado pelo meu metodo\nO produto vetorial eh :",i,"i",j,"j",k,"k")
    
    numpy = numpy.cross(v1,v2)
    print("pelo numpy eh :",numpy)
    


else:
    print("Erro")