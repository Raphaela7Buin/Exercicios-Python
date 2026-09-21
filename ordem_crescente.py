#ENTRADA DE DADOS
val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
val3 = int(input("Digite o terceiro valor: "))

#PROCESSAMENTO
numeros = [val1, val2, val3]
numeros.sort()

#sAIDA DE DADOS
print(f'Valores em ordem crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}')

#TESTES REALIZADOS
#ENTRADA: 8,15,4 -> Valores em ordem crescente: 4, 8, 15
#ENTRADA: 3,9,5 -> Valores em ordem crescente: 3    
#ENTRADA: -4,-1,-7 -> Valores em ordem crescente: -7, -4, -1