soma = 0
quantidade = 0
while True:
    num1 = int(input("Digite um valor: "))
    if num1 == 0:
        break
    
    soma = soma + num1
    quantidade = quantidade + 1
    media = soma/quantidade

print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma: {soma}")
print(f"Média: {media}")
