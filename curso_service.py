class  Curso:
    def __init__(self, id, curso, nivel):
        self.id = id
        self.curso = curso
        self.nivel = nivel

class CursoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

    def adicionar(self, curso, nivel):
        if not curso or not nivel:
            raise Exception("Curso e nivel são obrigatórios")
        for curso in self.lista:
            if curso.curso == curso:
                raise Exception("Curso já existe")
        id = self.proximo_id
        curso = Curso(id, curso, nivel)
        self.lista.append(curso)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for curso in self.lista:
            if curso.id == id:   
                return curso    
        return None 
    
    def atualizar (self, id, curso, nivel):
        curso = self.buscar_por_id(id)
        if curso:
            curso.curso = curso
            curso.matricula = nivel

    def remover (self, id):
        for curso in self.lista:
            if curso.id == id:
                self.lista.remove(curso)
                break
