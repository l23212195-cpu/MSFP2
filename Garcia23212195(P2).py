"""
Práctica 2: Diseño de controladores

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Garcia Grijalva Armando
Número de control: 23212195
Correo institucional: L23212195@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl
import pandas as pd
from scipy import signal as sg

# datos de la simulacion
u = np.array(pd.read_excel('signal.xlsx',header=None))
x0,t0,tend,dt,w,h = 0,0,15,1E-3,10,5
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)
u = np.reshape(u,-1)
signal = ["Lazo abierto","Hipotenso","Hipertenso"]

"""Componentes del circuito RLC y funcion de transferencia en base al caso:
n = Normotenso
l = Hipotenso
h = Hipertenso
"""

""" Normotenso """
# componentes del circuito RLC y funcion de transferencia
Zn,Ln,Rn,Cn = 10E3,1E-3,1,1.5
numN = [0.001,0.010]
denN = [0.000015,0.001010,0.010]
sysN = ctrl.tf(numN,denN)
print(f"Funcion de transferencia de Normotenso: {sysN}\n")
# polos del sistema 
Ln = np.roots(denN)
print(f"polos del sistema: L1 = {Ln[0]:.3e}, L2 = {Ln[1]:.3e}\n")
# Funciones del sistema en lazo abierto
def openloop(t, sysN, u):
    _,PpN = ctrl.forced_response(sysN, t, u, x0)
    return PpN

""" Hipotenso """
# componentes del circuito RLC y funcion de transferencia
Zl,Ll,Rl,Cl = 10E3,1E-3,1,3.5
numL = [0.001,0.010]
denL = [0.000035,0.001010,0.010]
sysL = ctrl.tf(numL,denL)
print(f"Funcion de transferencia de Normotenso: {sysL}\n")
# polos del sistema 
Ll = np.roots(denL)
print(f"polos del sistema: L1 = {Ll[0]:.3e}, L2 = {Ll[1]:.3e}\n")
kPl, kIl, kDl = 480.078, 1219332.260, 0.006
Crl = 1E-6
Rel = 1/(Crl*kIl)
Rrl = kPl*Rel
Cel = kDl/Rrl
numPIDl = [Rel*Rrl*Cel*Crl, Rel*Cel + Rrl*Crl, 1]
denPIDl = [Rel*Crl, 0]
PIDl = ctrl.tf(numPIDl, denPIDl)
print(f"El valor de la capacitancia Cr es de {Crl} Faradios.\n")
print(f"El valor de la resistencia Re es de {Rel} Ohms.\n")
print(f"El valor de la resistencia Rr es de {Rrl} Ohms.\n")
print(f"El valor de la capacitancia Ce es de {Cel} Faradios.\n")
print(f"Función de transferencia del controlador PID: {PIDl}\n")
# Sistema de control en lazo cerrado
sysPIDl = ctrl.feedback(ctrl.series(PIDl, sysL), 1, sign = -1)
print(f"Función de transferencia del sistema de control en lazo cerrado: {sysPIDl}\n")
# Funciones del sistema en lazo abierto y lazo cerrado
def openloop(t, sysL, u):
    _,PpL = ctrl.forced_response(sysL, t, u, x0)
    return PpL
def closedloop(t, sysPIDl, u):
    _,PIDl = ctrl.forced_response(sysPIDl, t, u, x0)
    return PIDl

""" Hipertenso """
# componentes del circuito RLC y funcion de transferencia
Zh,Lh,Rh,Ch = 10E3,1E-3,1,1
numH = [0.001,0.010]
denH = [0.000010,0.001010,0.010]
sysH = ctrl.tf(numH,denH)
print(f"Funcion de transferencia de Normotenso: {sysH}\n")
# polos del sistema 
Lh = np.roots(denH)
print(f"polos del sistema: L1 = {Lh[0]:.3e}, L2 = {Lh[1]:.3e}\n")
kPh, kIh, kDh = 311.480, 1796432.503, 0.0017
Crh = 1E-6
Reh = 1/(Crh*kIh)
Rrh = kPh*Reh
Ceh = kDh/Rrh
numPIDh = [Reh*Rrh*Ceh*Crh, Reh*Ceh + Rrh*Crh, 1]
denPIDh = [Reh*Crh, 0]
PIDh = ctrl.tf(numPIDh, denPIDh)
print(f"El valor de la capacitancia Cr es de {Crh} Faradios.\n")
print(f"El valor de la resistencia Re es de {Reh} Ohms.\n")
print(f"El valor de la resistencia Rr es de {Rrh} Ohms.\n")
print(f"El valor de la capacitancia Ce es de {Ceh} Faradios.\n")
print(f"Función de transferencia del controlador PID: {PIDh}\n")
# Sistema de control en lazo cerrado
sysPIDh = ctrl.feedback(ctrl.series(PIDh, sysH), 1, sign = -1)
print(f"Función de transferencia del sistema de control en lazo cerrado: {sysPIDh}\n")
# Funciones del sistema en lazo abierto y lazo cerrado
def openloop(t, sysH, u):
    _,PpH = ctrl.forced_response(sysH, t, u, x0)
    return PpH
def closedloop(t, sysPIDh, u):
    _,PIDh = ctrl.forced_response(sysPIDh, t, u, x0)
    return PIDh

# Colores
clr1 = np.array([255, 212, 68])/255
clr2 = np.array([85, 169, 160])/255
clr3 = np.array([40, 122, 116])/255
clr4 = np.array([188, 2, 2])/255
clr5 = np.array([131, 0, 0])/255

# Respuestas de los 3 casos
for i in range(0,3):
    if i == 0: # Lazo abierto
        PpN = openloop(t, sysN, u)
        PpL = openloop(t, sysL, u)
        PpH = openloop(t, sysH, u)
        fg = plt.figure(i+1)
        fg.set_size_inches(w,h)
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman']
        plt.plot(t, PpN, '-', linewidth = 0.5, color = clr1, label='Pp(t): Normotenso')
        plt.plot(t, PpL, '--', linewidth = 0.5, color = clr2, label='Pp(t): Hipotenso')
        plt.plot(t, PpH, ':', linewidth = 0.5, color = clr4, label='Pp(t): Hipertenso')
    if i == 1: # Hipotenso
        PpN = openloop(t, sysN, u)
        PpL = openloop(t, sysL, u)
        PIDl = openloop(t, sysPIDl, u)
        fg = plt.figure(i+1)
        fg.set_size_inches(w,h)
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman']
        plt.plot(t, PpN, '-', linewidth = 0.5, color = clr1, label='Pp(t): Normotenso')
        plt.plot(t, PpL, '--', linewidth = 0.5, color = clr2, label='Pp(t): Hipotenso')
        plt.plot(t, PIDl, ':', linewidth = 0.5, color = clr3, label='Pp(t): Hipotenso_PID')
    if i == 2: # Hipertenso
        PpN = openloop(t, sysN, u)
        PpH = openloop(t, sysH, u)
        PIDh = openloop(t, sysPIDh, u)
        fg = plt.figure(i+1)
        fg.set_size_inches(w,h)
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman']
        plt.plot(t, PpN, '-', linewidth = 0.5, color = clr1, label='Pp(t): Normotenso')
        plt.plot(t, PpH, '--', linewidth = 0.5, color = clr4, label='Pp(t): Hipertenso')
        plt.plot(t, PIDh, ':', linewidth = 0.5, color = clr5, label='Pp(t): Hipertenso_PID')
    plt.xlim(0, 15); plt.xticks(np.arange(0, 16, 1))
    plt.ylim(-0.4, 1.2); plt.yticks(np.arange(-0.4, 1.4, 0.2))
    plt.xlabel('t[s]')
    plt.ylabel('Vi(t) [V]')
    plt.legend(bbox_to_anchor = (0.5, -0.25), loc = 'center', ncol = 3, frameon = False)
    plt.show()
    fg.savefig(signal[i] + '_Python.pdf', bbox_inches = 'tight')