# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:33:54 2020

@author: edunu
"""

# Gastos del piso
import pandas as pd
gastos = pd.read_excel("C:/Users/edunu/OneDrive/Escritorio/gastos-del-piso.xlsx")

# Diccionario, los nombres son las claves y la deuda de cada uno es el valor
deudas = dict()
nombres = {"A": "Avelina", "E": "Eduardo", "J": "Jesús", "L": "Laura",
           "N": "Noelia", "X": "Extranjero"}
# A = Avelina
# E = Edu
# J = Jesús
# L = Laura
# N = Noelia
deuditas = dict()
for name in list(nombres.keys()): # Para cada nombre
    deuda = list() # Lista que contiene cada deuda individual, se reinicia con
                   #     cada nombre.
    for _ in range(len(gastos)):
        if name != "X": # Para evitar errores por deudas de gente de fuera
            if name in gastos["Quién"][_]:
                if name not in gastos["ParaQuién"][_]:
                    deuda.append(-gastos["Cuánto"][_])
                elif name in gastos["ParaQuién"][_]:
                    deuda.append(gastos["Cuánto"][_]/len(gastos["ParaQuién"][_]) - gastos["Cuánto"][_])
            elif name not in gastos["Quién"][_]:
                if name in gastos["ParaQuién"][_]:
                    deuda.append(gastos["Cuánto"][_]/len(gastos["ParaQuién"][_]))
        elif name == "X":
            for i in range(gastos["ParaQuién"][_].count("X")):
                deuda.append(gastos["Cuánto"][_]/len(gastos["ParaQuién"][_]))
    deudas[name] = round(sum(deuda), 2)
    deuditas[name] = deuda
    print(nombres[name], "debe %.2f euros." % sum(deuda))
    
# Print output
tabla = dict()
for name in list(nombres.keys()): # Persona que debe [0]
    deuda = dict()
    for nombre in list(nombres.keys()): # Persona a quien le debe [1]
        deudita = list()
        for _ in range(len(gastos)):
            if name != nombre and name in gastos["ParaQuién"][_] and nombre in gastos["Quién"][_]:
                deudita.append(gastos["Cuánto"][_]/len(gastos["ParaQuién"][_]))
        deuda[nombre] = sum(deudita)
    tabla[name] = deuda

pd.DataFrame(tabla)
tabla = pd.DataFrame.from_dict(tabla, orient = "index").transpose()           
            
            












db = 


