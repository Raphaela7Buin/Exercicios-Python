# ENTRADA DE DADOS
numero = int(input("Digite um número: "))

# PROCESSAMENTO E SAÍDA DE DADOS
if numero % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

print(f"Resultado: {resultado}")

# Testes realizados:
# Entrada: 12 -> Resultado: PAR
# Entrada: 13 -> Resultado: ÍMPAR