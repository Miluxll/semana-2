n= int(input("Ingresa un numero: "))
if n>= 20:
    x= 1
    f= 1
while x <= n:
    f = f * x
    x += 1
print(f"El factorial de {n} es {f} ")
else;
print("No se puede calcular")

