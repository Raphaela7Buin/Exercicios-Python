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