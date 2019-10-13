# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:45:37 2018


A continuación, crearemos el programa de una calculadora básica, los cálculos que debe cubrir son:
     1 Sumar
     2 Restar
     3 Multiplicar
     4 Dividir

"""

# Programa calculadora
# Declaricion de variables
opcion = 0

# Declaracion de Funciones1
def suma(a, b):
    ## TODO ##
    return a+b

def resta(a,b):
    ## TODO ##
    return a-b

def multiplicar(a,b):
    ## TODO ##
    return a*b

def dividir(a,b):
    ## TODO ##
    return a/b

# Inicio del programa

while ('5' != opcion):
    opcion = input('''Por favor seleccione una operacion:
     1 Sumar
     2 Restar
     3 Multiplicar
     4 Dividir
     5 Salir
     ''')

    if (opcion == '1'):
        ## TODO ##
        a=int(input("Por favor seleccione un sumando:"))
        b=int(input("Por favor seleccione otro sumando:"))
        resultado =suma(a,b)
        print ("El resultado es: "+str(resultado))
        ## TODO ##
    elif opcion == '2':
        ## TODO ##
        a=int(input("Por favor seleccione un valor:"))
        b=int(input("Por favor seleccione otro valor que restarle:"))
        resultado = resta(a,b)
        print ("El resultado es: "+str(resultado))
        ## TODO ##
    elif opcion == '3':
       ## TODO ##
        a=int(input("Por favor seleccione un valor que multiplicar:"))
        b=int(input("Por favor seleccione otro valor que que multiplicar:"))
        resultado = multiplicar(a,b)
        print ("El resultado es: "+str(resultado))
        ## TODO ##
    elif opcion == '4':
        ## TODO ##
        a=int(input("Por favor seleccione un numerador:"))
        b=int(input("Por favor seleccione un denominador:"))
        resultado = dividir(a,b)
        print ("El resultado es: "+str(resultado))
        ## TODO ##
    elif opcion == '0' or opcion>'5':
        ## TODO ##
        continue
    if (opcion!= '5'):
        input("Pulse Enter para continuar...")

print('Fin del programa')