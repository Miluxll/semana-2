num = int(input("Ingresa un numero: "))
x= 1
c= 0
while x<= num:
         if num % x == 0:
           c = c + 1
         x = x + 1
if c == 2:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo")
