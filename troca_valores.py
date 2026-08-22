#ENTRADA DOS DADOS
a = int(input("A: "))
b = int(input("B: "))

#PROCESSAMENTO DOS DADOS(troca com variavél auxiliar)
auxiliar = a
a = b
b = auxiliar

#SAÍDA DOS DADOS
print("\nDepois da troca:")
print(f"A: {a}")
print(f"B: {b}")

#TESTES FEITOS:
#ENTRADA: A = 1, B = 2 -> SAÍDA: A = 2, B = 1
#ENTRADA: A = -5, B = 10 -> SAÍDA: A = 10, B = -5
#ENTRADA: A = 7, B = 7 -> SAÍDA: A = 7, B = 7
