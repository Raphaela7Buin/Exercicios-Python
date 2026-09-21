#ENTRADA DE DADOS
num1 =float(input("Primeiro valor: ").replace(',','.'))
num2 =float(input("Segundo valor: ").replace(',','.'))
num3 =float(input("Terceiro valor: ").replace(',','.'))

#PROCESSAMENTO
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

#FUNÇÃO AUXILIAR PARA FORMATAR NUMEROS INTEIROS SEM O .0
def formatar(valor):
    return int(valor) if valor.is_integer() else valor

#SAIDA DE DADOS
print(f'Maior {formatar(maior)}')
print(f'Menor {formatar(menor)}')

#TESTES REALIZADOS
#ENTRADA: 8,15,4 -> Maior 15, Menor 4
#ENTRADA: 3,9,5 -> Maior 9, Menor 3
#ENTRADA: -4,-1,-7 -> Maior -1, Menor -7
#ENTRADA: 6,6,2 -> Maior 6, Menor 2

