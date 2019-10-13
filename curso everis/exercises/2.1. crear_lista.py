"""
Created on Wed Apr  4 12:28:41 2018
"""

"""
Crea un programa donde se defina una función llamada crear_lista que cree una lista de números a partir 
de los elementos que vaya pidiendo por pantalla. Esta función toma como argumentos el número de 
elementos que va a pedir al usuario y retorna la lista creada.

En la función main() pide el número de elementos mediante input() y almacénalo en la variable numero

Haz la llamada a la función crear_lista y pásale como argumento esa variable num.
Finalmente, imprime por pantalla la lista resultante.
"""


def crear_lista(num):
    lista = []
    
    if num < 1:
        print("¡Imposible!")
    else:
        while len(lista) <= num:
            lista.append(len(lista))
            
    return lista


def main():
    
    numero = int(input("Dígame cuántos valores tiene la lista: "))
    lista= crear_lista(numero)
    print("La lista creada es:", lista)
    
    
if __name__ == '__main__':
    main() 