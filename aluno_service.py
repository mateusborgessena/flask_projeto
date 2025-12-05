class Aluno:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula


class AlunoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1


        self.adicionar("Maria Silva", "2023801")
        self.adicionar("João Pereira", "2023802")
        self.adicionar("Ana Costa", "2023003")

    def adicionar(self, nome, matricula):
        novo_aluno = Aluno(self.proximo_id, nome, matricula)
        self.lista.append(novo_aluno)
        self.proximo_id += 1

    def listar(self):
        return self.lista
