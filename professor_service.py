class  professor:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula
class ProfessorService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1
        self.adicionar("Ana Braga", "2025137")
        self.adicionar("Jorge Batista", "2029510")
        self.adicionar("Maria Costa", "2023141")

    def adicionar(self, nome, matricula):
        id = self.proximo_id
        professor = professor(id, nome, matricula)
        self.lista.append(professor)
        self.proximo_id += 1

    def listar(self):
        return self.lista
