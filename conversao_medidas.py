#ENTRADA DE DADOS
metros= float(input("Metros: ").replace(',','.'))

#PROCESSAMENTO DE DADOS
centimetros = metros * 100
milimetros = metros * 1000

#SAIDA DE DADOS
print(f"Centímetros: {centimetros:g}")
print(f"Milímetros: {milimetros:g}")

#TESTES REALIZADOS:
#ENTRADA: 1 -> Centímetros: 100 | Milímetros: 1000
#ENTRADA: 0.75 -> Centímetros: 75 | Milímetros: 750
#ENTRADA: 12.3 -> Centímetros: 1230 | Milímetros: 12300
