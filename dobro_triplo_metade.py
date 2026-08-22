#ENTRADA DE DADOS 
numero = float(input("Digite um valor: ").replace(',','.'))

#PROCESSAMENTO DE DADOS 
dobro = numero * 2
triplo = numero * 3
metade = numero / 2

#SAIDA DE DADOS (REMOVE OS DECIMAIS DESNECESSÁRIOS  SE O RESULTADOR FOR INTEIRO)
print(f"Dobro: {dobro:g}")
print(f"Triplo: {triplo:g}")
print(f"Metade: {metade:g}")

#VALORES DE TESTE
*Entrada: 8 , Dobro: 16, Triplo: 24, Metade: 4
*Entrada: 2,5 , Dobro: 5, Triplo: 7,5, Metade: 1,25
*Entrada: -4 , Dobro: -8, Triplo: -12, Metade: -2