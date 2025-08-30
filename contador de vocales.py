def cu_vocal(texto):
    vocales= "aeiou"
    contador= 0
    longitud= len(texto)
    for i in range(longitud):
        letra= texto.lower()[i]
        if letra in vocales:
            contador += 1
    return contador

texto= input("Texto: ")
contador=cu_vocal(texto)
print(f"El numer de vocales es de: {contador}")
