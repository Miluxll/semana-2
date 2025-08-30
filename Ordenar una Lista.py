lista= []
print("Elementos desiados: ")
canti=int(input())
i = 0
while i < canti:
    print("Ingresar elementos: ", i+1)
    nombre = input()
    lista.append(nombre)
    i + 1
    lista.sort()
    print(lista)
