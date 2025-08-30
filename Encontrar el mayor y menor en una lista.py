entrada_usuario = input("Ingresa números separados por espacios: ")
try:
    numeros_str = entrada_usuario.split() 
    numeros = [float(num) for num in numeros_str]
    if not numeros:
        print("No se ingresaron números.")
    else:
        numero_mayor = max(numeros)
        numero_menor = min(numeros)
        print(f"El número mayor es: {numero_mayor}")
        print(f"El número menor es: {numero_menor}")
except ValueError:
    print("Entrada no válida. Por favor, ingresa solo números.")
