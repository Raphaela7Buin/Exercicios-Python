#ENTRADA DE DADOS
nota1 = float(input("Nota 1:").replace(",","."))
nota2 = float(input("Nota 2:").replace(",","."))

#PROCESSAMENTO DE DADOS
media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#SAIDA DE DADOS
print(f"\nMédia: {media:.1f}".replace(".",","))
print(f"Situação: {situacao}")

#TESTES REALIZADOS
# Teste 1: nota1 = 8, nota2 = 9 -> Média    = 8.5, Situação = Aprovado
# Teste 2: nota1 = 5, nota2 = 6 -> Média    = 5.5, Situação = Reprovado 
