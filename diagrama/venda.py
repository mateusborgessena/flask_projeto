class Aluno:
    def __init__(self, nome , cpf ):
        self.nome = nome
        self.cpf = cpf
class Disciplina:
    def __init__(self, nome , valor ):
        self.nome = nome
        self.valor = valor
class Historico:
    def __init__(self, cliente , data_Aluno ):
        self.Aluno = cliente
        self.data_Aluno = data_Aluno
        self.itens = []
def adicionar_item(self, Disciplina):
    self.itens.append(Disciplina)
    print(f"Disciplina'{Disciplina.nome}'adicionado ao curricolo.")

def calcular_total(self):
    total = 0
    for produto in self.itens:
        total += produto.itens
    return total

def resumo(self):
    print("\n--- RESUMO DA VENDA ---")
    print(f"Cliente: {self.cliente.nome}")
    print(f"CPF: {self.cliente.cpf}")
    print(f"Data da venda: {self.data_venda}")
    print("Itens:")
    for p in self.itens:
        print(f"- {p.nome} | R$ {p.valor:.2f}")
    print(f"Total de itens: {len(self.itens)}")
    print(f"Valor total: R$ {self.calcular_total():.2f}")

   
cliente1 = Cliente("João da Silva", "123.456.789-00")

venda = Venda(cliente1, "03/12/2025")

produto1 = Produto("Arroz", 7.50)
produto2 = Produto("Detergente", 2.30)
produto3 = Produto("Fita adesiva", 4.20)

venda.adicionar_item(produto1)
venda.adicionar_item(produto2)
venda.adicionar_item(produto3)

venda.resumo()
