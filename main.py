# Solicita ao usuário a entrada de um número inteiro não negativo
numero = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número informado é negativo
if numero < 0:
    
    # Se for negativo, exibe uma mensagem de erro
    print("O número deve ser não negativo.")
    
else:
    
    # Inicializa uma variável para armazenar o fatorial do número
    fatorial = 1
    
    # Imprime a mensagem inicial indicando o cálculo do fatorial
    print("Cálculo do fatorial de", numero, ":")

    # Loop para multiplicar os números de 1 até o número informado
    for multiplicador in range(1, numero + 1):
        
        # Multiplica o valor atual de 'fatorial' pelo número atual na iteração
        fatorial *= multiplicador
        
        # Imprime o número da iteração atual seguido de "!" e o símbolo de igual
        print(f"{multiplicador}! =", end=" ")

        # Loop para imprimir a expressão do fatorial (e.g., "1 * 2 * 3")
        for i in range(1, multiplicador + 1):
            
            print(i, end="")
            
            if i != multiplicador:
                
                # Imprime o símbolo de multiplicação se não for o último número
                print(" * ", end="")
                
        # Imprime o resultado parcial do fatorial para a iteração atual
        print(" = ", fatorial)

    # Imprime o resultado final, que é o fatorial do número informado pelo usuário
    print("O fatorial de", numero, "é:", fatorial)
