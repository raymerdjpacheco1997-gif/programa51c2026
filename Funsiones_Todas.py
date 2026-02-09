def suma_lista(lista):
    """
    Recibe una lista de números y calcula la suma total
    """
    total = 0
    for numero in lista:
        total = total + numero
    return total

# Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
resultado = suma_lista(numeros)
print("Eduardo Salinas - Suma total:", resultado)

#Edwin Espinosa 8-1023-293
def calcular_promedio(lista):
    if not lista:  # Verificamos que la lista no esté vacía para evitar error de división por cero
        return 0
    
    suma_total = sum(lista)
    cantidad_elementos = len(lista)
    promedio = suma_total / cantidad_elementos
    
    return promedio

# Ejemplo de uso:
mis_numeros = [10, 8, 9, 7, 10]
resultado = calcular_promedio(mis_numeros)

print(f"La lista es: {mis_numeros}")
print(f"El promedio es: {resultado}")


#      Grupo 6
# Raiz cuadrada - Ecuacion-lineal 
# Desarrollado por: Isacar Hernandez y Eimy Mendez

def obtener_negativos(lista):
    return [n for n in lista if n < 0]


#se hace una lista donde imprima los numeros negativos
def obtener_positivos(lista):
    return [n for n in lista if n > 0]

#Numero ingresados
mi_lista = [10, -5, 8, -1, -22, 15]
print(f"Isacar Hernandez: Negativos son {obtener_negativos(mi_lista)}")

#imprimir numero positivos
print(f"Eimy Mendez:  los numeros positivos son {obtener_positivos(mi_lista)}")



#