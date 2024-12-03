from buscar_banco import *
import locale
import pandas as pd

valor_caixa = 0
@staticmethod
def formatar_dinheiro(valor):
    # Define a localidade para formatar o valor em formato brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    # Método para formatar o valor em formato monetário brasileiro
    return locale.currency(valor, grouping=True)
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
def requests_caixa(valor=None, request='get'):
    global valor_caixa  # Para modificar a variável global
    
    if request == 'get':
        return f"Valor atual do caixa: {formatar_dinheiro(valor_caixa)}"
    
    if valor is None or not isinstance(valor, (int, float)):
        return "Erro: Valor inválido ou não fornecido."
    
    if request == 'post':
        if valor < 0:
            return "Erro: Não é possível adicionar valores negativos ao caixa."
        valor_caixa += valor
        return f"Valor de {formatar_dinheiro(valor)} adicionado ao caixa. Total: {formatar_dinheiro(valor_caixa)}"
    
    if request == 'remove':
        if valor < 0:
            return "Erro: Não é possível remover valores negativos do caixa."
        if valor > valor_caixa:
            return "Erro: Valor insuficiente no caixa para a remoção."
        valor_caixa -= valor
        return f"Valor de {formatar_dinheiro(valor)} removido do caixa. Total: {formatar_dinheiro(valor_caixa)}"
    
    return "Erro: Operação inválida. Use 'get', 'post' ou 'remove'."
def requests_quantidade(codigo_produto,quantidade,request='remove'):

    planilha_produtos = openpyxl.load_workbook('produtos.xlsx')
    
    # Função interna para atualizar o status do produto na aba fornecida
    def atualizar_status_aba(aba_produtos):
        pagina_produtos = planilha_produtos[aba_produtos]
        for linha in pagina_produtos.iter_rows(values_only=True, min_row=2):  # Iterar pelas células
            codigo_cell, nome_cell, valor_cell, validade_cell, quantidade_cell, status_cell = linha

            if codigo_cell.lower() == codigo_produto.lower():
                if request == 'remove':
                    if quantidade_cell - quantidade <0:
                        print(f'O produto {nome_cell} não tem estoque suficiente para quantidade desejada')
                    else:
                        print(f'quantidade do produto {nome_cell} atualizada com sucesso')
                        quantidade_cell -= quantidade
                        return True
                if request == 'post':
                    quantidade_cell += quantidade
                    print(f'quantidade do produto {nome_cell} atualizada com suceso')
                    return True
                else:
                    print("tipo de request não econtratada utilize(post ou remove))")
            else:
                print("codigo do produto não encontrado ")
        return False  

    # Atualiza nas duas abas: Produtos Normais e Produtos Eletrônicos
    if atualizar_status_aba('Produtos Normais') or atualizar_status_aba('Produtos Eletrônicos'):
        # Salva a planilha com as alterações
        planilha_produtos.save('produtos.xlsx')
    else:
        print("quantidade não atualizada.")
def buscar_preco_produtos(lista_codigos):
    # Carregar o arquivo Excel fornecido
    file_path = 'produtos.xlsx'
    # Carregar todas as abas do Excel em um dicionário de dataframes
    produtos_dict = pd.read_excel(file_path, sheet_name=None)

    # Concatenar todas as abas em um único dataframe
    produtos_df = pd.concat(produtos_dict.values(), ignore_index=True)

    valor_total = 0.0
    for codigo_produto, quantidade in lista_codigos:
        # Filtrar o dataframe para encontrar o produto com o código fornecido
        produto = produtos_df[produtos_df['Código do Produto'] == codigo_produto.upper()]
        
        # Verificar se o produto foi encontrado
        if not produto.empty:
            valor_total += produto['Valor Unitário'].values[0] * quantidade
    return round(valor_total, 2)

