# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:33:54 2020

@author: edunu
"""

# Gastos del piso
import pandas as pd
gastos = pd.read_excel("C:/Users/edunu/OneDrive/Escritorio/git/gastos-del-piso.xlsx")

# Diccionario, los nombres son las claves y la deuda de cada uno es el valor
nombres = {"A": "Avelina", "E": "Eduardo", "J": "Jesús", "L": "Laura",
           "N": "Noelia", "X": "Extranjero"}
# A = Avelina
# E = Edu
# J = Jesús
# L = Laura
# N = Noelia
tabla = dict()
for name in list(nombres.keys()): # Persona que debe [0]
    deuda = dict()
    for nombre in list(nombres.keys()): # Persona a quien le debe [1]
        deudita = list()
        for _ in range(len(gastos)):
            if name != nombre and name in gastos["ParaQuién"][_] and nombre in gastos["Quién"][_]:
                for i in range(gastos["ParaQuién"][_].count(name)):
                    deudita.append(round(gastos["Cuánto"][_]/len(gastos["ParaQuién"][_]), 2))
        deuda[nombre] = sum(deudita)
    tabla[name] = deuda

del deudita, deuda, gastos
tabla = pd.DataFrame.from_dict(tabla, orient = "index").transpose()           

print("#######################################\n" +
      "# ESTAS SON LAS CUENTAS DEL MADRIPISO #\n" +
      "#######################################\n")

print("¿Cuánto debe cada uno a cada uno?\n")
for name in list(nombres.keys()):
    for nombre in list(nombres.keys()):
        if name != nombre and tabla[nombre][name] != 0:
            print("%s debe %.2f euros a %s." % (nombres[nombre], 
                                          tabla[nombre][name],
                                          nombres[name]))

print("\n\n\n" +
      "#################\n" +
      "# SIMPLIFICANDO #\n" +
      "#################\n")

print("Pero, haciendo cuentas, ¿cuánto debe realmente\n" +
      "cada uno a cada uno?\n")

k = len(list(nombres.keys()))
i = 0 # Esto es un contador para evitar repeticiones como "Avelina debe 0 a Avelina"
for name in list(nombres.keys()):
    i +=1
    for nombre in list(nombres.keys())[i:k]:
        if tabla[nombre][name] != 0:
            if tabla[nombre][name] > tabla[name][nombre]:
                print("%s debe %.2f euros a %s." % (nombres[nombre], 
                                          tabla[nombre][name] - tabla[name][nombre],
                                          nombres[name]))
            elif tabla[name][nombre] > tabla[nombre][name]:
                print("%s debe %.2f euros a %s." % (nombres[name], 
                                          tabla[name][nombre] - tabla[nombre][name],
                                          nombres[nombre]))

print("\n\n\n" +
      "######################\n" +
      "# PARA LOS PEREZOSOS #\n" +
      "######################\n")

print("¿Te da pereza buscar tu nombre entre tanta línea?")

inicial = input("Dime cuál es tu inicial y te lo pondré más fácil: ")
print("")
if inicial in "aejlnxAEJLNX":
    inicial = inicial.upper()
    k = len(list(nombres.keys()))
    i = 0 # Esto es un contador para evitar repeticiones como "Avelina debe 0 a Avelina"
    for name in list(nombres.keys()):
        i +=1
        for nombre in list(nombres.keys())[i:k]:
            if tabla[nombre][name] != 0:
                if nombre == inicial or name == inicial:
                    if tabla[nombre][name] > tabla[name][nombre]:
                        print("%s debe %.2f euros a %s." % (nombres[nombre], 
                                                  tabla[nombre][name] - tabla[name][nombre],
                                                  nombres[name]))
                    elif tabla[name][nombre] > tabla[nombre][name]:
                        print("%s debe %.2f euros a %s." % (nombres[name], 
                                                  tabla[name][nombre] - tabla[nombre][name],
                                                  nombres[nombre]))    
del name  , inicial, i, k
print("\n\n\n###########\n" +
      "# TOTALES #\n" +
      "###########\n")            
print("En total, ¿cuánto debe cada uno, o cuánto\n" +
      "se le debe a cada uno?\n")
for nombre in list(nombres.keys()):
    debe = pd.DataFrame.sum(tabla, axis = 0)[nombre]
    se_le_debe = pd.DataFrame.sum(tabla, axis = 1)[nombre]
    total = debe - se_le_debe
    if total > 0:
        print("%s debe %.2f euros." % (nombres[nombre], 
                                  total))
    elif total < 0:
        print("A %s se le debe(n) %.2f euros." % (nombres[nombre], 
                                  -1 * total))  
del nombre, debe, se_le_debe, total, nombres