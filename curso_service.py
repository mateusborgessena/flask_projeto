class  Curso:
    def __init__(self, id, nome, nivel):
        self.id = id
        self.nome = nome
        self.nivel = nivel

class CursoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        self.adicionar("Informatica", "Superior")
        self.adicionar("Saneamento", "Medio")
        self.adicionar("Vestuario", "Medio")

    def adicionar(self, curso, nivel):
        id = self.proximo_id
        novo_curso = Curso(id, nivel, curso)
        self.lista.append(novo_curso)
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

    def remover (self, id, curso, nivel):
        curso = self.buscar_por_id(id)
        if curso:
            curso.curso = curso
            curso.nivel = nivel
