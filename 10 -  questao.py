import math

num: int
somaPares: int
somaPrimos: int
contPrimo: int

contPrimo = 0
somaPares = 0
somaPrimos = 0
for n in range(1, 4):
    num = int(input("Digite um número: "))
    
    if num % 2 == 0:
        somaPares += num

    for m in range(1, int(math.sqrt(num)+1)):
        if num % m == 0:
            contPrimo += 1

    if contPrimo == 0:
        somaPrimos += num
    
print(f"Soma dos números pares: {somaPares}")
print(f"Soma dos números primos: {somaPrimos}")

