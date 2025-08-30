import sys
def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num 
    return suma
def main():
    num_str = input("Ingrese numeros: ")
    try:
        num_list = [int(num) for num in num_str.split(',')]
    except ValueError:
        print("Deben ser números separados por comas: ")
        sys.exit()
    suma = suma_lista(num_list)
    print(f"La suma de los elementos de la lista de: {suma}")

if __name__ == '__main__':
    main()
