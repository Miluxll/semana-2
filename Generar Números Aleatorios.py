from random import randint
n = int(input("Ingrese cuántos números aleatorios desea obtener: "))
num_aleatorio =[randint(1,100) for i in range (n)]
print(num_aleatorio  )
