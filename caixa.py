import locale
from funcoes import *

# Define a localidade para formatar o valor em formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Caixa:
    def __init__(self, valor_inicial):
        # Inicializa o caixa com o valor inicial fornecido
        self.valor = valor_inicial
        # Dicionário para armazenar os produtos no estoque
        
        print(f"Caixa iniciado com {self.formatar_dinheiro(self.valor)}")

    def gerenciar_estoque(self):
       while True:
            print('1. cadastrar produtos')
            print('2. pesquisar produtos')
            print('3. remover produtos')
            print('4. voltar')
           
            opcao = input_usuario("Escolha uma opção (1 a 4): ",tipo=int)
            if opcao == 1:
                adicionar_produto_interativo()
            elif opcao == 2:
                pesquisando_produto()
            elif opcao == 3:
                removendo_produtos()
            elif opcao == 4:
                break
            else:
                print("\nOpção inválida. Por favor, escolha de 1 a 4.\n")
           


           

    def vender_no_caixa(self):
        # Método para realizar uma venda no caixa
        print("\nVender no Caixa:")
        produto = input("Nome do produto: ")
        if produto in self.estoque:
            quantidade = int(input("Quantidade a vender: "))
            if quantidade <= self.estoque[produto]['quantidade']:
                # Calcula o valor total da venda e atualiza o valor do caixa
                total = quantidade * self.estoque[produto]['preco']
                self.valor += total
                # Atualiza a quantidade do produto no estoque
                self.estoque[produto]['quantidade'] -= quantidade
                print(f"Venda realizada com sucesso. Valor total: {self.formatar_dinheiro(total)}")
            else:
                print("Quantidade insuficiente no estoque.")
        else:
            print("Produto não encontrado no estoque.")

    def relatorios_dos_produtos(self):
        while True:
            print('1. pesquisar produtos de ate x dias')
            print('2. pesquisar produtos de ate x quantidade')
            print('3. voltar')
            opcao = input_usuario("Escolha uma opção (1 a 3): ",tipo=int)
            if opcao == 1:
                dias_prod = input_usuario('digite a quantidade de dias: ',tipo=int)
                mostrar_produtos_filtrados(validade=dias_prod)
            elif opcao == 2:
                quantidade_prod = input_usuario('digite a quantidade: ',tipo=int)
                mostrar_produtos_filtrados(quantidade=quantidade_prod)
            elif opcao == 3:
                break
            else:
                print("\nOpção inválida. Por favor, escolha de 1 a 3.\n")
         
                
    def fechar_caixa(self):
        # Método para fechar o caixa e mostrar o valor final
        print(f"\nCaixa fechado com valor final de {self.formatar_dinheiro(self.valor)}")

    @staticmethod
    def formatar_dinheiro(valor):
        # Método para formatar o valor em formato monetário brasileiro
        return locale.currency(valor, grouping=True)

def main():
    #valor inicial para abrir o caixa
    valor_inicial = input_usuario("Digite o valor para abrir o caixa: R$ ",tipo=float)
    caixa = Caixa(valor_inicial)
            
        
    # Menu principal do caixa
    while True:
        print("\nOpções do Caixa:")
        print("1. Gerenciar Estoque")
        print("2. Vender no Caixa")
        print("3. Relatório dos Produtos")
        print("4. Fechar Caixa")
        
        opcao = input_usuario("Escolha uma opção (1 a 4): ",tipo=int)
        if opcao == 1:
            # Chama o método para gerenciar o estoque
            caixa.gerenciar_estoque()
        elif opcao == 2:
            # Chama o método para realizar uma venda no caixa
            caixa.vender_no_caixa()
        elif opcao == 3:
            # Chama o método para gerar o relatório dos produtos
            caixa.relatorios_dos_produtos()
        elif opcao == 4:
            # Chama o método para fechar o caixa e encerra o programa
            caixa.fechar_caixa()
            break
        else:
            print("Opção inválida. Por favor, escolha de 1 a 4.")
        

if __name__ == "__main__":
    main()
