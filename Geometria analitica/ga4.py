#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:01:07 2019

@author: sergio
"""

import numpy

#comentario do programa enviado pelo facebook
print("Este programa resolve o exercício 07 da lista 02 de maneira geral.")
print("\nO usuário digita os 3 vetores e o resultado dos 3 produtos escalares.")
print("\nO programa se encarrega de montar as matrizes dos coeficientes,")
print("\no vetor coluna dos termos independentes, e calcula o vetor necessário")
print("que é a solução do sistema linear\n")


# coordenada dos vetores sem ter que fazer uma função
print("Digite as coordenas separadas por virgurlas, ex: 1,3,4")
v1 = eval('[' + input("Digite as coordenadas do vetor 1: ") + ']')
v2 = eval('[' + input("Digite as coordenas do vetor 2: ") + ']')
v3 = eval('[' + input("Digite as coordenas do vetor 3: ") + ']')
#valor produto escalar
print("\nDigite o valor do primeiro produto escalar")
k1 = int(input("Digite o valor de k1: " ))
print()
print("Digite o valor do segundo produto escalar")
k2 = int(input("Digite o valor de k2: " ))
print()
print("Digite o valor do terceiro produto escalar")
k3 = int(input("Digite o valor de k3: " ))
#matriz
A = numpy.array( [ v1,v2,v3 ])
#vetor coluna
B = numpy.array([[k1],[k2],[k3]])
#resolve o sistema linear
x = numpy.linalg.solve(A,B)
print("A matriz dos coeficientes é\n",A)
print("O vetor coluna é\n",B)


print("o valor de x é ",x[0][0])
print("o valor de y é ",x[1][0])
print("o valor de z é ",x[2][0])