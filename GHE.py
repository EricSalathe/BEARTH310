#!/bin/python3
S = 2650
a = 0.7
T = 735

sig = 5.67e-8
Rin = 1/4*(1 - a)*S
Rg = sig*T**4

Ratm = Rg - Rin
Rt = Rin - Ratm
tau = Rt/Rg

print(tau*100)
