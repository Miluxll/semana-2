def cant_de_pal(texto):
      texto_lim=texto.replace(",","")
      palabras=texto_lim.split()
      cant_de_pal= len(palabras)
      return cant_de_pal

mi_texto = input( "Ingrese un texto: ")
numero_palabras = cant_de_pal(mi_texto)
print(f"El texto tiene {numero_palabras} palabras.")
