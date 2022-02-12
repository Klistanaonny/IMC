# def= Função para calcular o imc.
def calcular_imc():
    # Variável para o Peso.
    peso = float(input('\nSeu peso: '))

    # Variável para a Altura.
    altura = float(input('Sua altura: '))

    # Calculo do IMC.
    imc = peso / (altura**2)

    # Mostrar o resultado final.
    print(f'seu imc é de: {imc}')

    # Executar a função para rodar o programa novamente.
    novamente()


# Função para iniciar o programa novamente.
def novamente():
    # Mostrar as opções.
    print('\nVocê deseja calcular novamente?')

    # Variável da resposta, para saber se vai seguir ou não.
    resposta = input('Digite "S" para sim, e "N" para não: ')

    # Se a resposta for SIM, executa o programa novamente.
    if resposta.upper() == "S":
        calcular_imc()

    # Se a resposta for NÃO, não faz nada.
    # else + if
    # .upper() faz com que ele transforme toda variável em maiúscula.
    elif resposta.upper() == "N":
        print('\nObrigada!')

    # Se não for um caractere válido vai perguntar novamente.
    else:
        novamente()


# Executar a função para calcular o IMC.
calcular_imc()
