import os

idade: int
op: int
regular: int
bom: int
otimo: int
mediaIdadeOtimo: float
somaIdadeOtimo: float
perBom: float

otimo = 0
bom = 0
idade = 0
op = 0
mediaIdadeOtimo = 0
somaIdadeOtimo = 0
regular = 0

for n in range(1, 16):
    idade = int(input("Informe sua idade: "))
    op = int(input("\nÓtimo — 3\nBom — 2\nRegular — 1\nInforme sua opinião:"))

    os.system("cls")
    somaIdadeOtimo += idade

    if op == 3:
        otimo += 1
        somaIdadeOtimo += idade
    if op == 1:
        regular += 1
    if op == 2:
        bom += 1

mediaIdadeOtimo = somaIdadeOtimo / otimo
perBom = bom / 15 * 100

print("Média de idades de pessoas que responderam ótimo: ", mediaIdadeOtimo)
print("Quantidade de pessoas que responderam: ", regular)
print("Percentagem de pessoas que responderam bom: ", perBom)