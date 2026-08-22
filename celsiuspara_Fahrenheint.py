#ENTRADA DE DADOS 
celsius = float(input("Temperatura em °C: ").replace(",", "."))

#PROCESSAMENTO
fahrenheit = (celsius * 9/5) + 32

#SAÍDA DE DADOS
print(f"Temperatura em °F: {fahrenheit:g}")

#TESTES REALIZADOS:
#ENTRADA: 0 -> Temperarura em °F: 32
#ENTRADA: 100 -> Temperatura em °F: 212
#ENTRADA: -40 -> Temperatura em °F: -40

