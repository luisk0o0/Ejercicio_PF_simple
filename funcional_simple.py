from functools import reduce


palabras = ["Hola", "a", "todos", "los", "compañeros", "de", "el", "grupo", "de", "compiladores"]


def convertir_a_mayusculas(palabra):
    return palabra.upper()


def filtrar_palabras_largas(palabra):
    return len(palabra) > 5           #Consideramos las palabras largas a las que tienen mas de letras


def concatenar_palabras(acumulador, palabra):
    return f"{acumulador} {palabra}" #acumulador + " " + palabra


palabras_mayusculas = list(map(convertir_a_mayusculas, palabras))


palabras_largas = list(filter(filtrar_palabras_largas, palabras))


frase_concatenada = reduce(concatenar_palabras, palabras)

print("Palabras originales:", palabras)
print("Palabras en mayúsculas:", palabras_mayusculas)
print("Palabras largas:", palabras_largas)
print("Frase concatenada:", frase_concatenada)