
#vou criar uma funcao para fazer isso 

def inversor(texto):
    return texto[::-1] #assim eu inverto 
# cada letra oculpa uma posicao comecando do "0" dessa forma inverto
escrita= input("Digite o texto que será invertido:  ")
texto_invertido= inversor(escrita)
print(f"String invertida:{texto_invertido} ")


# Outra forma 
'''
texto="Chocolate"
invertido = texto[::-1]
print(f"O texto invertido é :{invertido} ")

'''

