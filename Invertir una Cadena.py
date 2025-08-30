texto_original = input("Ingresa un texto: ")
texto_invertido= ""
for character in texto_original:
    texto_invertido = character +texto_original
    print(f"El texto invertido es {texto_invertido}")
