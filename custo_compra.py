#ENTRADA DE DADOS
preco_unitario = float(input("Preço unitário: R$ ").replace('.','').replace(',','.'))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ ").replace('.','').replace(',','.'))

#PROCESSAMENTO DOS DADOS 
subtotal = preco_unitario * quantidade
total = subtotal + frete

#SAÍDA DOS DADOS
print(f"Subtotal: R$ {subtotal:.2f}".replace('.',','))
print(f"Total: R$ {total:.2f}".replace('.', ','))

#TESTES REALIZADOS:
#ENTRADA: 10.00, 3, 5.00 -> Subtotal: R$ 30,00 | Total: R$ 35,00    
#ENTRADA: 49.90, 2, 0.00 -> Subtotal: R$ 99,80 | Total: R$ 99,80
#ENTRADA: 7.50, 10, 12.00 -> Subtotal: R$ 75,00 | Total: R$ 87,00
