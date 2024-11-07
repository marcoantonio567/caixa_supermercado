import locale

# Define a localidade para formatar o valor em formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Caixa:
    def __init__(self, valor_inicial):
        # Inicializa o caixa com o valor inicial fornecido
        self.valor = valor_inicial
        # Dicionário para armazenar os produtos no estoque
        self.estoque = {}
        print(f"Caixa iniciado com {self.formatar_dinheiro(self.valor)}")

    def gerenciar_estoque(self):
        # Método para gerenciar o estoque de produtos
        while True:
            print("\nGerenciar Estoque:")
            print("1. Adicionar produto")
            print("2. Atualizar quantidade")
            print("3. Voltar")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    # Adiciona um novo produto ao estoque
                    produto = input("Nome do produto: ")
                    quantidade = int(input("Quantidade: "))
                    preco = float(input("Preço unitário: R$ "))
                    self.estoque[produto] = {'quantidade': quantidade, 'preco': preco}
                    print(f"Produto {produto} adicionado com sucesso!")
                elif opcao == 2:
                    # Atualiza a quantidade de um produto existente no estoque
                    produto = input("Nome do produto a atualizar: ")
                    if produto in self.estoque:
                        quantidade = int(input("Quantidade a adicionar ou remover: "))
                        self.estoque[produto]['quantidade'] += quantidade
                        print(f"Estoque do produto {produto} atualizado para {self.estoque[produto]['quantidade']}.")
                    else:
                        print("Produto não encontrado no estoque.")
                elif opcao == 3:
                    # Volta ao menu principal
                    break
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

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
        # Método para exibir um relatório dos produtos no estoque
        print("\nRelatório dos Produtos:")
        for produto, info in self.estoque.items():
            print(f"Produto: {produto}, Quantidade: {info['quantidade']}, Preço Unitário: {self.formatar_dinheiro(info['preco'])}")

    def fechar_caixa(self):
        # Método para fechar o caixa e mostrar o valor final
        print(f"\nCaixa fechado com valor final de {self.formatar_dinheiro(self.valor)}")

    @staticmethod
    def formatar_dinheiro(valor):
        # Método para formatar o valor em formato monetário brasileiro
        return locale.currency(valor, grouping=True)

def main():
    while True:
        try:
            # Solicita ao usuário o valor inicial para abrir o caixa
            valor_inicial = float(input("Digite o valor para abrir o caixa: R$ "))
            caixa = Caixa(valor_inicial)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

    # Menu principal do caixa
    while True:
        print("\nOpções do Caixa:")
        print("1. Gerenciar Estoque")
        print("2. Vender no Caixa")
        print("3. Relatório dos Produtos")
        print("4. Fechar Caixa")
        try:
            opcao = int(input("Escolha uma opção (1 a 4): "))
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
        except ValueError:
            print("Entrada inválida. Por favor, digite um número (1 a 4).")


if __name__ == "__main__":
    main()
