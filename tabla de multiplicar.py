numero=int(input("Ingrese un numero: "))
if numero >0 :
    for i in range(11):
      total=numero*i
      print(f"{numero} por {i} es igual a {total}")
else:
    print("ingrese otro numero: ")
    
