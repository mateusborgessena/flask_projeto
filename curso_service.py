class  Curso:
    def __init__(self, id, nome, nivel):
        self.id = id
        self.nome = nome
        self.nivel = nivel

class CursoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

    def adicionar(self, nome, nivel):
        self._validar_dados(nome, nivel)
        id = self.proximo_id
        curso = Curso( id, nome , nivel)
        self.lista.append(curso)
        self.proximo_id +=1
        
    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for curso in self.lista:
            if curso.id == id:   
                return curso    
        return None 
    
    def atualizar(self,id,nome,nivel):
        self._validar_dados(nome,nivel,id)
        curso = self.buscar_por_id(id)
        if curso:
            curso.nome = nome
            curso.nivel = nivel
    
    def _validar_dados(self, nome, nivel, id=None):
        if not nome or not nivel:
            raise Exception("Nome e matrícula são obrigatórios")
        for curso in self.lista:
            if curso.nome == nome:
                if id is None or curso.id != id:
                    raise Exception("Nome já existe")

    def remover (self, id):
        for curso in self.lista:
            if curso.id == id:
                self.lista.remove(curso)
                break
