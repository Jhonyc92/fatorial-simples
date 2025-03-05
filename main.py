# Solicita ao usuário a entrada de um número inteiro não negativo
numero = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número informado é negativo
if numero < 0:
    
    # Se for negativo, exibe uma mensagem de erro
    print("O número deve ser não negativo.")
    
else:
    
    # Inicializa uma variável para armazenar o fatorial do número
    fatorial = 1

    # Loop que percorre todos os números inteiros de 1 até o número informado pelo usuário (inclusive)
    for i in range(1, numero + 1):
        
        # Multiplica o valor atual de 'fatorial' pelo número atual (i) na iteração
        # fatorial = fatorial * i
        fatorial *= i

    # Imprime o resultado final, que é o fatorial do número informado pelo usuário
    print("O fatorial de", numero, "é:", fatorial)
    
