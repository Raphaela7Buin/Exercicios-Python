#ENTRADA DE DADOS
salario_fixo = float(input("Salario fixo: R$ ").replace('.','').replace(',','.'))
total_vendido = float(input("Total vendido: R$ ").replace('.','').replace(',','.'))

#CÁLCULO DA COMISSÃO
comissao = total_vendido *0.04
salario_total = salario_fixo + comissao

#SAÍDA DE DADOS
print(f'Comissão: R$ {comissao:.2f}'.replace('.', ','))
print(f'Salário total: R$ {salario_total:.2f}'.replace('.', ','))

#TESTES FEITOS:
#Entrada: 1500.00 e 5000.00  -> Comissão: R$ 200,00 | Salário total: R$ 1.700,00
#Entrada: 2000.00 e 0.00     -> Comissão: R$ 0,00   | Salário total: R$ 2.000,00
#Entrada: 2500.00 e 20000.00 -> Comissão: R$ 800,00 | Salário total: R$ 3.300,00