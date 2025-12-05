class  Professor:
    def __init__(self, id, nome, cpf, disciplina):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina

class ProfessorService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        self.adicionar("Ana Braga", "2025137", "Historia")
        self.adicionar("Jorge Batista", "2029510", "Portugues")
        self.adicionar("Maria Costa", "2023141", "Matematica")

    def adicionar(self, nome, cpf, disciplina):
        id = self.proximo_id
        novo_professor = Professor(id, nome, cpf, disciplina)
        self.lista.append(novo_professor)
        self.proximo_id += 1

    def listar(self):
        return self.lista
