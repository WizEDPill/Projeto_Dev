fatura_estados={
   "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}# Dicionario
#calculando o faturamento total 
total_faturamento= sum(fatura_estados.values())
# Cálculo do percentual 
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in  fatura_estados.items()}

print("Percentual de representacao do faturamento mensal por cada estado:   ")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
    