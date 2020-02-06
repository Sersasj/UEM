#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:37:02 2019

@author: sergio
"""
i = 0
resultado = 0
v = []

print("Este programa calcula o vetor paralelo tal que vetor1*vetor2=k")
r = int(input("Digite a dimensao desejada: "))
print("\nDigite as coordenas separadas por virgurlas, ex: 1,3,4")
u1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
k = float(input("Digite uma constante k, tal que u*v=k : "))
#funçao para achar o produto escalar de u1
while i < r:
    resultado += u1[i]*u1[i]
    i +=1

i = 0
#encontrar x
x = k/resultado

"""funçao para fazer u1*x para encontrar v.
queria fazer imprimir igual o exercio3a (o vetor v é: x,y,z)
mas não consegui, essa função imprime os valores um embaixo do outro
seguindo a ordem x,y,z... respectivamente"""
while i < r:
    v = u1[i]*x    
    print("\nAs coordenadas do vetor v sao respectivamente:",v)
    i +=1
       
       