#ENTRADA DE DADOS 
largura = float(input("Largura: ").replace(',','.'))
altura = float(input("Altura: ").replace(',','.'))

#PROCESSAMENTO DE DADOS 
area = largura * altura
perimetro = 2 * (largura + altura)

#SAIDA DE DADOS 
print(f"Área: {area:g}")
print(f"Perímetro: {perimetro:g}")

#TESTES REALIZADOS: 
#ENTRADA: 4 e 4 -> Área: 16 | Perímetro: 16
#ENTRADA: 2.5 e 8 -> Área: 20 | Perímetro: 21
#ENTRADA: 10 e 1 -> Área: 10 | Perímetro: 22
