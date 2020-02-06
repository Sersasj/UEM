#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:23:48 2019

@author: sergio
"""
import math

print("Este programa calcula a coordenada cartesiana de um vetor")
print("Digite o radiano como no exemplo: 0.541 \n ")
radiano1 = float(input("Digite o angulo diretor alfa em radianos: "))
radiano2 = float(input("Digite o angulo diretor beta em radianos: "))
radiano3 =  float(input("Digite o angulo diretor gamma em radianos:"))
modulo =  float(input("digite o modulo do vetor: "))
#tranforma radiano em cosseno
cos1 = math.cos(radiano1)
cos2 = math.cos(radiano2)
cos3 = math.cos(radiano3)
#calcula a coordenada do vetor
v1 = modulo*cos1
v2 = modulo*cos2
v3 = modulo*cos3

print("A coordenadas cartesianas do vetor é aproximadamente: ",v1,",",v2,",",v3)
