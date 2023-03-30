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

# Loop principal do programa
while True:
    print("=== Menu ===")
    print("1. Registrar produto")
    print("2. Registrar venda")
    print("3. Consultar produto")
    print("0. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        registrar_produto()
    elif opcao == 2:
        registrar_venda()
    elif opcao == 3:
        consultar_produto()
    elif opcao == 0:
        # Salva os dados no arquivo antes de sair
        with open("produtos.pickle", "wb") as arquivo:
            pickle.dump(produtos, arquivo)
            break