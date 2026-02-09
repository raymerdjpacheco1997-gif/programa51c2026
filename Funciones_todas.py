def obtener_negativos(lista):
    return [n for n in lista if n < 0]

def obtener_positivos(lista):
    return [n for n in lista if n > 0]

mi_lista = [10, -5, 8, -1, -22, 15]
print(f"Isacar Hernandez: Negativos son {obtener_negativos(mi_lista)}")
print(f"Eimy: Positivos son {obtener_positivos(mi_lista)}")