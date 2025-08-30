cadena = input("Ingresa un texto: ")
n= input("Ingresa el carácter que deseas contar: ")
j=0
for i in cadena :
    if n==i:
        j=j+1
print(f"El carácter {n} se encuentra {j} veces")
