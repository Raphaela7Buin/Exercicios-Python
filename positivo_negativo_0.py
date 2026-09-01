# ENTARDA DE DADOS
numero = float(input("Digite um número: ").replace(',', '.'))

# PROCESSAMENTO E SAÍDA DE DADOS
if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print(f"Resultado: {resultado}")

# Testes realizados:
# Entrada: 12   -> Resultado: POSITIVO
# Entrada: -0.5 -> Resultado: NEGATIVO
# Entrada: 0    -> Resultado: ZERO