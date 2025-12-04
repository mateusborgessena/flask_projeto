class Venda:
    def __init__(self, nome_cliente, data_venda):
        self.nome_cliente = nome_cliente
        self.data_venda = data_venda
        self.itens = []   

    def adicionar_item(self, nome_produto):
        if nome_produto.strip() != "":
            self.itens.append(nome_produto)
            print(f"Produto '{nome_produto}' adicionado à venda.")
        else:
            print("Nome de produto inválido!")

    def resumo(self):
        print("\n--- RESUMO DA VENDA ---")
        print(f"Cliente: {self.nome_cliente}")
        print(f"Data da venda: {self.data_venda}")
        print("Itens:")
        for p in self.itens:
            print(f"- {p}")
        print(f"Total de itens: {len(self.itens)}")

