#Lista maximo-lista facorial
#**********************************************
#**     Desarrollado por Cristian Castillo     **

def factorial_lista(lista):
    resultado = []
    for n in lista:
        if n < 0:
            resultado.append(None)  # No existe factorial de negativos
        else:
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            resultado.append(fact)

    print("Lista original:", lista)
    print("Factoriales:", resultado)
    return resultado

numeros = [3, 5, 0, 4]
factorial_lista(numeros)
print("Hecho por Cristian Castillo")
