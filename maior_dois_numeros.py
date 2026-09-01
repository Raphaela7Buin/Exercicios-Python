#ENTRADA DOS DADOS 

num1 = float(input("Primeiro valor: ").replace(",", "."))
num2 = float(input("Segundo valor: ").replace(",", "."))

#PROCESSAMENTO E SAIDA DOS DADOS
if num1 > num2:
 #FORMATAÇÃO LIMPA PRA EXIBIR INTEIROS SEM .0
    print(f"Maior valor: {int(num1) if num1.is_integer() else num1}")
elif num2 > num1:
    print(f"Maior valor: {int(num2) if num2.is_integer() else num2}")
else:
    print("Os valores são iguais.")

#TESTES REALIZADOS
#ENTRADA: 12 e 7 -> Maior valor: 12
#ENTRADA: 4 e 9 -> Maior valor: 9
#ENTRADA: -2 e -8 -> Maior valor: -2
#ENTRADA: 5 e 5 -> Os valores são iguais.
#ENTRADA: 10 e 10 -> Os valores são iguais.
    