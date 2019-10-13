# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:48:16 2018

"""
"""
Crear un programa para validación de nombres de usuarios. Dicho programa,
deberá cumplir con los siguientes requisitos:

Tener una función llamada 'validar' con tres argumentos (nombre,minimo,maximo). Se encargará
de:

    Comprobar que la longitud de nombre no es menor que el mínimo,
    en caso contrario retornar el mensaje:
    "El nombre de usuario debe contener al menos 'minimo' caracteres".


    Comprobar que la longitud de nombre no es mayor que el máximo,
    en caso contrario retornar el mensaje:
    "El nombre de usuario no puede ser de más de 'maximo' caracteres".


    Comprobar que ni la primera letra ni la última coinciden,
    encaso contrario retornar el mensaje:
    "El nombre de usuario no puede comenzar ni terminar por el mismo caracter"
    

Si todo es correcto imprimir por pantalla: "El nomnbre de usuario '",nombre,"' es válido."
     

"""

def validar(nombre, minimo,maximo):
    if  len(nombre)< minimo:
        print("El nombre de usuario debe contener al menos "+str(minimo) +" caracteres")
        
    if len(nombre)> maximo:
        print("El nombre de usuario no puede ser de más de "+str(maximo) +" caracteres")
        
    if nombre[0]==nombre[-1]:
        print("El nombre de usuario no puede comenzar ni terminar por el mismo caracter")
        
    elif minimo<=len(nombre) and len(nombre)<= maximo and nombre[0]!=nombre[-1] :
        print("El nomnbre de usuario "+ nombre+" es válido.")
    
    
    
    
def main():
    ## TODO ##
    nombre = str(input("Dígame un nombre: "))
    minimo = int(input("Dígame un minimo: "))
    maximo = int(input("Dígame un maximo: "))
    
    validar(nombre, minimo,maximo)

if __name__ == '__main__':
    main()   
    
    
    