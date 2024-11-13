import openpyxl
import re

def exibir_produtos(aba_produtos):
    planilha_produtos = openpyxl.load_workbook('produtos.xlsx')
    pagina_produtos = planilha_produtos[aba_produtos]

    for linha in pagina_produtos.iter_rows(values_only=True, min_row=2):
        codigo_produto, nome_produto, valor_produto, validade, quantidade, status = linha
        print(f"Código: {codigo_produto}")
        print(f"Nome: {nome_produto}")
        print(f"Valor: {valor_produto}")
        print(f"Validade: {validade}")
        print(f"Quantidade: {quantidade}")
        print(f"Status: {status}")
        print('-' * 40)  # Para separar visualmente cada produto
def mostrar_todos_produtos():
    exibir_produtos('Produtos Normais')
    exibir_produtos('Produtos Eletrônicos')

def extrair_dias(validade):
    # Usamos regex para capturar o número antes de "dias"
    match = re.match(r"(\d+)\s*dia[s]?", validade)
    if match:
        return int(match.group(1))
    return 0  # Retorna 0 caso não consiga extrair o número

def filtrar_produtos(aba_produtos, nome=None, quantidade=None, validade=None, codigo=None,status_ativo=True):

    planilha_produtos = openpyxl.load_workbook('produtos.xlsx')
    pagina_produtos = planilha_produtos[aba_produtos]

    for linha in pagina_produtos.iter_rows(values_only=True, min_row=2):
        codigo_produto, nome_produto, valor_produto, validade_produto, quantidade_produto, status = linha
        
        # Filtro baseado nos critérios
        if nome.lower() not in nome_produto.lower():#aqui ta retirando os nomes diferentes do input
            continue
        if quantidade and quantidade_produto < quantidade:#aqui ta retirando as quantidadas diferentes do input
            continue
        if validade != extrair_dias(validade_produto):
            continue
        if status_ativo and status.lower() != "ativo":#aqui ta retirando os stataus desativos
            continue
        if codigo and str(codigo) != str(codigo_produto).strip():
            continue
        
        # Exibe os produtos que atendem aos critérios
        print(f"Código: {codigo_produto}")
        print(f"Nome: {nome_produto}")
        print(f"Valor: {valor_produto}")
        print(f"Validade: {validade_produto}")
        print(f"Quantidade: {quantidade_produto}")
        print(f"Status: {status}")
        print('-' * 40)  # Para separar visualmente cada produto

def mostrar_produtos_filtrados(codigo=None,nome=None, quantidade=None, validade=None):

    filtrar_produtos('Produtos Normais', nome, quantidade, validade,codigo)
    filtrar_produtos('Produtos Eletrônicos', nome, quantidade, validade,codigo)

# Exemplo de uso
mostrar_produtos_filtrados(quantidade=11)
