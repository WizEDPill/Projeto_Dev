import json 

# Ler os dados Json
def ler_data_json(arquivo):
    with open(arquivo, "r") as l: 
       dados= json.load(l)
       return[float(dia["valor"]) for dia in dados]
        


# calcular o faturamento
def calcular_faturamento(dados): 
    data_converte=[float(valor)for valor in dados]
    men_valor= min(valor for valor in data_converte if valor>0) #exclui dias com valor zero
    mai_valor= max(data_converte)
    dados_validos = [valor for valor in data_converte if valor > 0]
    media_mensal= sum(dados_validos)/len(dados_validos) # soma dos dados dividio pelo tamanho
    dias_acima_media= sum(1 for valor in data_converte if valor > media_mensal)
   
    return men_valor, mai_valor, media_mensal, dias_acima_media
#executável-main
if __name__== "__main__": 
    # lendo os dados 
    data_json= ler_data_json('dados.json')

    # chamando a funcao para as variaveis 
    men_valor, mai_valor, media_mensal, dias_acima_media = calcular_faturamento(data_json)


    # resultados: 
    print(f"Menor valor de faturamento foi : R$ {men_valor:.2f}")
    print(f"Maior valor de faturamento foi : R$ {mai_valor:.2f}")
    print(f"Media mensal de faturamento foi : R$ {media_mensal:.2f}")
    print(f"'Dias com faturamento acima da média : R$ {dias_acima_media:.2f}")



    