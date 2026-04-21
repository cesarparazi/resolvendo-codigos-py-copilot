# solicitar ao usuário que entre com  dois números, após isso, solicitar que escolha uma operação 
# matemática, os valores resultantes devem ser absolutos, por fim, exibir o resultado da opera
# ção escolhida entre os dois números.


# Solicitar dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicitar a operação
operacao = input("Escolha uma operação (+, -, *, /): ")

# Calcular o resultado e torná-lo absoluto
if operacao == '+':
    resultado = abs(num1 + num2)
elif operacao == '-':
    resultado = abs(num1 - num2)
elif operacao == '*':
    resultado = abs(num1 * num2)
elif operacao == '/':
    if num2 != 0:
        resultado = abs(num1 / num2)
    else:
        print("Erro: Divisão por zero!")
        exit()
else:
    print("Operação inválida!")
    exit()

# Exibir o resultado
print(f"O resultado absoluto da operação é: {resultado}")
    
 
