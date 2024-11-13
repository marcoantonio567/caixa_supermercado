import pandas as pd
import random
from datetime import datetime, timedelta
import openpyxl

# Gerar listas de produtos normais e eletrônicos
nomes_produtos_normais = [
    "Sabonete", "Shampoo", "Condicionador", "Detergente", "Esponja de Aço", "Sabão em Pó", "Amaciante", "Desinfetante",
    "Pasta de Dente", "Escova de Dente", "Papel Higiênico", "Toalha de Banho", "Travesseiro", "Colchão", "Caderno",
    "Lápis", "Caneta", "Borracha", "Tesoura", "Régua", "Copo Plástico", "Prato", "Faca", "Garfo", "Colher",
    "Panela", "Frigideira", "Escorredor", "Ralador", "Forma de Bolo", "Garrafa Térmica", "Vassoura", "Rodo",
    "Pano de Chão", "Tapete", "Lençol", "Travesseiro", "Cobertor", "Abajur", "Mesa", "Cadeira", "Armário",
    "Sofá", "Rack", "Estante", "Livro", "Quadro", "Espelho", "Almofada", "Relógio de Parede", "Lâmpada",
    "Cafeteira", "Chaleira", "Ferro de Passar", "Escova de Cabelo", "Pente", "Shampoo Infantil", "Condicionador Infantil",
    "Jogo de Lençol", "Jogo de Toalhas", "Avental", "Luvas de Cozinha", "Assadeira", "Forma de Pizza", "Cortador de Pizza",
    "Escumadeira", "Colher de Pau", "Pano de Prato", "Papel Toalha", "Gás de Cozinha", "Fósforos", "Isqueiro",
    "Câmera de Ar", "Pneu de Bicicleta", "Corrente de Bicicleta", "Capacete", "Joelheira", "Cotoveleira",
    "Jogo de Chaves", "Martelo", "Furadeira", "Parafusadeira", "Parafuso", "Prego", "Porca", "Arruela", "Chave de Fenda",
    "Chave Philips", "Alicate", "Trena", "Nível", "Serrote", "Arco de Serra", "Fita Isolante", "Fita Veda Rosca"
]

nomes_produtos_eletronicos = [
    "Televisão", "Celular", "Notebook", "Tablet", "Fone de Ouvido", "Mouse", "Teclado", "Monitor", "Câmera Digital",
    "Smartwatch", "Rádio", "DVD Player", "Home Theater", "Projetor", "Carregador Portátil", "Console de Videogame",
    "Controle Remoto", "Microondas", "Geladeira", "Freezer", "Ventilador", "Aspirador de Pó", "Purificador de Água",
    "Cafeteira Elétrica", "Batedeira", "Liquidificador", "Torradeira", "Sanduicheira", "Churrasqueira Elétrica",
    "Panela Elétrica", "Fritadeira Elétrica", "Ar Condicionado", "Aquecedor", "Lâmpada Inteligente", "Roteador",
    "Modem", "Receptor de TV", "Caixa de Som Bluetooth", "Amplificador", "Gravador Digital", "Playstation",
    "Xbox", "Kindle", "Câmera de Segurança", "Drone", "Controle de Drone", "Balança Digital", "Báscula Elétrica",
    "Telefone Sem Fio", "Telefone Fixo", "Smart TV", "Mousepad com LED", "Teclado Mecânico", "Caixa de Som Subwoofer",
    "Impressora", "Scanner", "Fax", "Caixa Registradora Elétrica", "Termômetro Digital", "Medidor de Pressão",
    "Oxímetro", "Estetoscópio Digital", "Secador de Cabelo", "Chapinha", "Barbeador Elétrico", "Aspirador Robô",
    "Estufa", "Pipoqueira Elétrica", "Videogame Portátil", "Adaptador Bluetooth", "Dock Station",
    "Carregador sem fio", "Bateria Externa", "Controle Universal", "Webcam", "Amplificador de Sinal",
    "Gravador de Voz", "Carregador USB para Carro", "Organizador de Cabos", "Cabo HDMI", "Cabo USB",
    "Adaptador de Tomada", "Protetor de Tela", "Suporte para Celular", "Lâmpada de Mesa USB", "Termoventilador",
    "Mini Geladeira Portátil", "Grill Elétrico", "Aquecedor de Mamadeira Elétrico", "Balança de Cozinha Digital",
    "Medidor de Energia", "Detector de Metais", "Fonte de Alimentação", "Luminária LED", "Ventilador USB",
    "Aquário com Filtro Elétrico", "Robô Aspirador de Pó com Mapeamento"
]

# Função para gerar status "Ativo" ou "Desativo"
def gerar_status():
    return random.choice(["Ativo", "Desativo"])

# Função para gerar validade em formato de dias
def gerar_validade():
    dias = random.randint(1, 365)  # Quantidade de dias aleatórios
    return f"{dias} dias"

# Gerar dados dos produtos normais
dados_produtos_normais = []
for i in range(1, 101):
    produto = {
        "Código do Produto": f"N{i:03}",
        "Nome do Produto": random.choice(nomes_produtos_normais),
        "Valor Unitário": round(random.uniform(5.0, 100.0), 2),
        "Validade": gerar_validade(),  # Usando a função para validade
        "Quantidade": random.randint(1, 10),
        "Status": gerar_status()  # Adicionando a coluna de status
    }
    dados_produtos_normais.append(produto)

# Gerar dados dos produtos eletrônicos
dados_produtos_eletronicos = []
for i in range(1, 101):
    produto = {
        "Código do Produto": f"E{i:03}",
        "Nome do Produto": random.choice(nomes_produtos_eletronicos),
        "Valor Unitário": round(random.uniform(50.0, 5000.0), 2),
        "Garantia": f"{random.randint(6, 24)} meses",
        "Quantidade": random.randint(1, 10),
        "Status": gerar_status()  # Adicionando a coluna de status
    }
    dados_produtos_eletronicos.append(produto)

# Criar DataFrames
df_normais = pd.DataFrame(dados_produtos_normais)
df_eletronicos = pd.DataFrame(dados_produtos_eletronicos)

# Escrever para um arquivo Excel com duas planilhas
with pd.ExcelWriter("produtos.xlsx") as writer:
    df_normais.to_excel(writer, sheet_name="Produtos Normais", index=False)
    df_eletronicos.to_excel(writer, sheet_name="Produtos Eletrônicos", index=False)
