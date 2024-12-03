from funcoes import *

class Caixa:
    def __init__(self, valor_inicial):
        requests_caixa(valor=valor_inicial,request='post')
        
        print(f"Caixa iniciado com {requests_caixa(request='get')}")
    
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
        lista_compras = []
        while True:
            print('1. adicionar codigo')
            print('2. Voltar')
            escolha = input_usuario('Escolha (1 ou 2): ',tipo=int)
            if escolha == 1:
                codigo_prod = input_usuario('qual o codigo do produto: ',tipo=str)
                if mostrar_produtos_filtrados(codigo=codigo_prod) == 'find':
                    quantidade_prod = input_usuario('digite a quantidade do produto: ',tipo=int)
                    lista_compras.append((codigo_prod,quantidade_prod))
                    total = buscar_preco_produtos(lista_compras)
                    print(f'valor total {total}')
                    while True:
                        print('1. passar outro produto')
                        print('2. finalizar compra')
                        proxima_compra = input_usuario('Escolha (1 ou 2): ',tipo=int)
                        if proxima_compra == 2:
                            print(f'sua compra deu {total}')
                            for produto in lista_compras:
                                requests_quantidade(codigo_produto=produto[0],quantidade=quantidade_prod,request='remove')
                            requests_caixa(valor=total,request='post')
                            break
                        elif proxima_compra == 1:
                            print("redirecionando para passar a compra")
                            break
                        else:
                            print("")
    
                elif mostrar_produtos_filtrados(codigo=codigo_prod) == 'nofind':
                    print('este produto não esta disponivel ou o codigo está errado')
            if escolha == 2:
                break
            else:
                print("por favor escolha uma opção valida")  
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
        print(f"\nCaixa fechado com valor final de {requests_caixa(request='get')}")

    

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
