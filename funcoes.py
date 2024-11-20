from buscar_banco import *


def input_usuario(texto, tipo=str):
    while True:
        try:
            if tipo == int:
                escolha = int(input(texto))
            elif tipo == float:
                escolha = float(input(texto))
            elif tipo == str:
                escolha = input(texto) 
            else:
                print("Tipo não suportado.")
                return None
            return escolha
        except ValueError:
            print("\nEntrada inválida, tente novamente.\n")
def adicionar_produto_interativo():
    while True:
        print('1. para adcionar produtos normais')
        print('2. para adcionar produtos eletronicos')
        print('3. Voltar')
        aba = input_usuario('Escolha (1 ,2 ,3): ',tipo=int)
        
        if aba == 1:
            aba = 'Produtos Normais'
            cod_prod = input("digite o codigo do produto: ")
            nome_prod = input_usuario("digite o nome do produto: ",tipo=str)
            valor_prod = input_usuario('digite o valor do produto: $ ',tipo=float)
            validade_prod = input_usuario('digite o validade do produto(em dias): ',tipo=int)
            quant_prod = input_usuario('digite o quantidade do produto: ',tipo=int)
            adicionar_produto(aba_produtos=aba,codigo=cod_prod,nome=nome_prod,valor=valor_prod,validade=validade_prod,quantidade=quant_prod,status='Ativo')
            
        elif aba == 2:
            aba = 'Produtos Eletrônicos'
            aba = 'Produtos Normais'
            cod_prod = input_usuario("digite o codigo do produto: ",tipo=str)
            nome_prod = input("digite o nome do produto: ")
            valor_prod = input_usuario('digite o valor do produto: $ ',tipo=float)
            validade_prod = input_usuario('digite a garantia do produto(em dias): ',tipo=int)
            quant_prod = input_usuario('digite o quantidade do produto: ',tipo=int)
            adicionar_produto(aba_produtos=aba,codigo=cod_prod,nome=nome_prod,valor=valor_prod,validade=validade_prod,quantidade=quant_prod,status='Ativo')
        elif aba == 3:
            break
        else:
            print('\nescolha uma opção valida\n')
def pesquisando_produto():
    while True:
        print('1. Para pesquisar por nome')  
        print('2. Para pesquisar por codigo')
        print('3. pesquisar todos os produtos')
        print('4. Voltar')
        escolha = input_usuario('Escolha (1 ,2 ,3 ,4): ',tipo=int)
        if escolha == 1:
            nome_prod = input_usuario("digite o nome do produto: ",tipo=str)
            mostrar_produtos_filtrados(nome=nome_prod)
            
        elif escolha == 2:
            cod_prod = input_usuario("digite o codigo do produto: ",tipo=str)
            mostrar_produtos_filtrados(codigo=cod_prod)
            
        elif escolha == 3:
            mostrar_todos_produtos()
            
        elif escolha == 4:
            break
        else:
            print('\nescolha uma opção valida\n')
def removendo_produtos():
    while True:
        print('realmente deseja algum produto?')
        print('1. proseguir')  
        print('2. Voltar')
    
        escolha = input_usuario('Escolha (1 ,2): ',tipo=int)
        if escolha == 1:
            cod_prod = input_usuario("digite o codigo do produto: ",tipo=str)
            desativar_produto(codigo_produto=cod_prod)
            break
        elif escolha == 2:
            break
        else:
            print('\nescolha uma opção valida\n')


