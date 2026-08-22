#ENTRADA DE DAODS 
preco = float(input("Preço: R$ ").replace(',', '.'))

#PROCESSAMENTO
desconto = preco * 0.10
preco_final = preco - desconto

#SAIDA DE DADOS (formatando com 2 casas decimais e trocando o ponto final pela virgula)
print(f"Desconto: R$ {desconto:.2f}".replace('.', ','))
print(f"Preço final: R$ {preco_final:.2f}".replace('.', ','))


#TESTES REALIZADOS:
#ENTRADA: 50.00 -> SAÍDA: Desconto: R$ 5,00 / Preço final: R$ 45,00
#ENTRADA: 99.90 -> SAÍDA: Desconto: R$ 9,99 / Preço final: R$ 89,91
#ENTRADA: 1000.00 -> SAÍDA: Desconto: R$ 100,00 / Preço final: R$ 900,00
