def pertence_fibonacci(numero):
    x,y = 0, 1 
    
    # verificando se o número é 0 ou 1 
    if numero== x or numero==y:
        return True
    
    # Gerando a sequencia até que o proximo número seja maior que o anterior
    while y < numero: 
        x, y = y, x + y  # valores sempre será a soma dos 2 valores anteriores
        if y ==numero: 
            return True
        
    return False
# verifica se o numero faz parte da sequência de Fibonnacci
numb= int(input("Informe um número: "))

if pertence_fibonacci(numb):
    print(f"Esse numero {numb} pertence à sequência de Fibonacci")
else: 
    print(f"Esse número {numb} nao pertence à sequência de Fibonacci ")