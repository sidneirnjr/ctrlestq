import tkinter as tk
from tkinter import ttk
import pickle


# Definição das funções de registro, venda e consulta de produtos

produtos = {}  # dicionário para armazenar os produtos


def registrar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_compra = float(input("Digite o valor de compra do produto: "))
    valor_venda = float(input("Digite o valor de venda do produto: "))
    lucro_estimado = (valor_venda - valor_compra) * quantidade

    produto = {"quantidade": quantidade, "valor_compra": valor_compra, "valor_venda": valor_venda,
               "lucro_estimado": lucro_estimado}
    produtos[nome] = produto


def registrar_venda():
    nome = input("Digite o nome do produto vendido: ")
    quantidade_vendida = int(input("Digite a quantidade vendida: "))
    produto = produtos.get(nome)

    if produto:
        quantidade_atual = produto["quantidade"]

        if quantidade_vendida > quantidade_atual:
            print("Quantidade inválida. Não há produtos suficientes para a venda.")
        else:
            novo_valor_estoque = quantidade_atual - quantidade_vendida
            novo_lucro_estimado = novo_valor_estoque * (produto["valor_venda"] - produto["valor_compra"])

            if novo_valor_estoque == 0:
                del produtos[nome]
            else:
                produtos[nome]["quantidade"] = novo_valor_estoque
                produtos[nome]["lucro_estimado"] = novo_lucro_estimado

            print("Venda registrada com sucesso!")
    else:
        print("Produto não encontrado.")


def consultar_produto():
    chave = input("Digite a palavra-chave para pesquisa: ")
    resultados = []

    for nome, produto in produtos.items():
        if chave in nome:
            resultados.append((nome, produto))

    if resultados:
        for nome, produto in resultados:
            print("=== Produto: ", nome, " ===")
            print("Quantidade: ", produto["quantidade"])
            print("Valor de compra: R$", produto["valor_compra"])
            print("Valor de venda: R$", produto["valor_venda"])
            print("Lucro estimado: R$", produto["lucro_estimado"])
    else:
        print("Nenhum produto encontrado para a palavra-chave informada.")


# Carregamento dos dados do arquivo, se existir
try:
    with open("produtos.pickle", "rb") as arquivo:
        produtos = pickle.load(arquivo)
except FileNotFoundError:
    pass


# criação da janela principal
root = tk.Tk()
root.geometry("800x600")
root.title("Controle de Estoque")

# definindo o estilo dos widgets
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# criação dos widgets

# frame para o registro de produtos
frame_registro = ttk.Frame(root, padding=20, relief="raised")
frame_registro.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# título do frame de registro de produtos
label_titulo_registro = ttk.Label(frame_registro, text="Registro de Produtos")
label_titulo_registro.grid(row=0, column=0, columnspan=2, pady=10)

# label e entry para o nome do produto
label_nome_produto = ttk.Label(frame_registro, text="Nome do Produto:")
label_nome_produto.grid(row=1, column=0, sticky="w")
entry_nome_produto = ttk.Entry(frame_registro, width=40)
entry_nome_produto.grid(row=1, column=1, padx=5, pady=5)

# label e entry para a quantidade do produto
label_quantidade = ttk.Label(frame_registro, text="Quantidade:")
label_quantidade.grid(row=2, column=0, sticky="w")
entry_quantidade = ttk.Entry(frame_registro, width=10)
entry_quantidade.grid(row=2, column=1, padx=5, pady=5)

# label e entry para o valor de compra do produto
label_valor_compra = ttk.Label(frame_registro, text="Valor de Compra (R$):")
label_valor_compra.grid(row=3, column=0, sticky="w")
entry_valor_compra = ttk.Entry(frame_registro, width=10)
entry_valor_compra.grid(row=3, column=1, padx=5, pady=5)

# label e entry para o valor de venda do produto
label_valor_venda = ttk.Label(frame_registro, text="Valor de Venda (R$):")
label_valor_venda.grid(row=4, column=0, sticky="w")
entry_valor_venda = ttk.Entry(frame_registro, width=10)
entry_valor_venda.grid(row=4, column=1, padx=5, pady=5)

# botão para registrar o produto
botao_registrar = ttk.Button(frame_registro, text="Registrar")
botao_registrar.grid(row=5, column=0, columnspan=2, pady=20)

# Criação dos widgets para o frame de registro de produtos
lbl_nome = tk.Label(frame_registro, text="Nome do produto:")
lbl_nome.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_nome = tk.Entry(frame_registro, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

lbl_qtd = tk.Label(frame_registro, text="Quantidade:")
lbl_qtd.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_qtd = tk.Entry(frame_registro, width=10)
entry_qtd.grid(row=1, column=1, padx=5, pady=5)

lbl_val_compra = tk.Label(frame_registro, text="Valor de compra:")
lbl_val_compra.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_val_compra = tk.Entry(frame_registro, width=10)
entry_val_compra.grid(row=2, column=1, padx=5, pady=5)

lbl_val_venda = tk.Label(frame_registro, text="Valor de venda:")
lbl_val_venda.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
entry_val_venda = tk.Entry(frame_registro, width=10)
entry_val_venda.grid(row=3, column=1, padx=5, pady=5)

btn_registrar = tk.Button(frame_registro, text="Registrar", command=registrar_produto)
btn_registrar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
