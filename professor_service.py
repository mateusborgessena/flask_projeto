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

    def adicionar(self, nome, cpf):
        if not nome or not cpf:
            raise Exception("Nome e matrícula são obrigatórios")
        for aluno in self.lista:
            if aluno.cpf == cpf:
                raise Exception("CPF já existe")
        id = self.proximo_id
        professor = Professor(id, nome, cpf,)
        self.lista.append(professor)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for professor in self.lista:
            if professor.id == id:   
                return professor    
        return None 
    
    def atualizar (self, id, nome, cpf, disciplina):
        professor = self.buscar_por_id(id)
        if professor:
            professor.nome = nome
            professor.disciplina = disciplina
            professor.cpf = cpf

    def remover (self, id):
        for professor in self.lista:
            if professor.id == id:
                self.lista.remove(professor)
                break
