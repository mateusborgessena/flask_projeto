class Aluno:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula


class AlunoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

    def adicionar(self, nome, matricula):
        id = self.proximo_id
        novo_aluno = Aluno(id, nome, matricula)
        self.lista.append(novo_aluno)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for aluno in self.lista:
            if aluno.id == id:   
                return aluno    
        return None 
    
    def atualizar (self, id, nome, matricula):
        aluno = self.buscar_por_id(id)
        if aluno:
            aluno.nome = nome
            aluno.matricula = matricula

    def remover (self, id, nome, matricula):
        aluno = self.buscar_por_id(id)
        if aluno:
            aluno.nome = nome
            aluno.matricula = matricula
    

        

