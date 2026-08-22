#ENTRADA DE DADOS
salario_atual = float(input("Salario atual: R$ ").replace('.', '').replace(',','.'))

#PROCESSAMENTO DOS DADOS
aumento = salario_atual * 0.15
novo_salario = salario_atual + aumento

#SAIDA DOS DADOS
print(f"Aumento: R$ {aumento:.2f}".replace('.', ','))
print(f"Novo salário: R$ {novo_salario:.2f}".replace('.', ','))

#VALORES DE TESTE:
#ENTRADA: 1200.00 -> Aumento: 180.00, Novo salário: 1380.00
#ENTRADA: 3500.00 -> Aumento: 525.00, Novo salário: 4025.00
#ENTRADA: 800.00 -> Aumento: 120.00, Novo salário: 920.00

