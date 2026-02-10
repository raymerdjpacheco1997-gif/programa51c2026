# *************
# Desarrollado por Raymer Pacheco
# *************
# inicia desarollo de la funcion dada 
# Función para contar el número de elementos en una lista. 
def contar_elementos_lista(elementos):
    # Contamos el número de elementos de la lista
    return len(elementos)

# Ejemplo de uso
lista_ejemplo = [1, 2, 3, 4, 5]
numero_de_elementos = contar_elementos_lista(lista_ejemplo)
print("El número de elementos en la lista es:", numero_de_elementos)

#*****************
#  FuncionG4
#*****************
# Desarrollar una funcion que reciba una lista
# y retorne el valor minimo
#*****************
# * Desarrollado por Angie De Gracia *
#*****************

# Funcion para identificar el numero minimo
def minimo(lista):
    menor = lista[0]

    for num in lista:
        if num < menor:
            menor = num

    return menor

# Descripcion del programa
print("Numero Mínimo")
print("Este programa arroja el numero entero de menor valor de una serie ingresada")

# Pedir cantidad de números
cantidad = int(input("¿Cuántos números deseas ingresar? "))

numeros = []

# Pedir números al usuario
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Calcular mínimo
resultado = minimo(numeros)

print("\nLos números ingresados son:", numeros)
print("El número mínimo es:", resultado, " - Desarrollado por Angie De Gracia")