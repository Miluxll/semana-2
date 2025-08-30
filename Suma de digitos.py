def sum_dig(num):
        s = 0
        while num > 0:
            s = s + num % 10
            num = num // 10
        return s
    
n = int(input("cantidad de numeros: "))
sum_total = 0
while n> 0:
    num=int(input("Numeros: "))
    sum_total = sum_total + sum_dig(num)
    n = n - 1
print(f"la suma total es de: {sum_total}")
