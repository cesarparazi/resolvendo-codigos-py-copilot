
# Solicitar os valores ao usuário
capital_inicial = float(input("Digite o capital inicial: "))
taxa_anual = float(input("Digite a taxa anual (em %): "))
periodo_meses = int(input("Digite o período em meses: "))

# Calcular a taxa mensal
taxa_mensal = taxa_anual / 100 / 12

# Listas para armazenar os valores mensais
meses = list(range(1, periodo_meses + 1))
montantes = []

# Calcular e exibir os montantes mês a mês
montante_atual = capital_inicial
for mes in meses:
    montante_atual *= (1 + taxa_mensal)
    montantes.append(montante_atual)
    print(f"Mês {mes}: R$ {montante_atual:.2f}")



