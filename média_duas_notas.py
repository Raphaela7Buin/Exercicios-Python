#ENTRADA DE DADOS 
nota1 = float(input("Nota 1: ").replace(',','.'))
nota2 = float(input("Nota 2: ").replace(',','.'))

#PROCESSAMENTO DE DADOS
media = (nota1 + nota2) / 2

#SAIDA FORMATADA COM UMA CASA DECIMAL
print(f"Média: {media:.1f}")


#NOTAS TESTADAS
nota1 = 5.5
nota2 = 7.5
nota3 = 10.0
nota4 = 9.0
nota5 = 0.0
nota6 = 4.0