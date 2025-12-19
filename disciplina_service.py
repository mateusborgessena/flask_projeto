class  Disciplina:
    def __init__(self, id, nome, carga_horaria, ementa):
        self.id = id
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.ementa = ementa

class DisciplinaService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

    def adicionar(self, nome, carga_horaria, ementa):
        id = self.proximo_id
        nova_disciplina = Disciplina(id, nome, carga_horaria, ementa)
        self.lista.append(nova_disciplina)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for disciplina in self.lista:
            if disciplina.id == id:   
                return disciplina    
        return None 
    
    def atualizar (self, id, nome, carga_horaria, ementa):
        disciplina = self.buscar_por_id(id)
        if disciplina:
            disciplina.nome = nome
            disciplina.carga_horaria = carga_horaria
            disciplina.ementa = ementa

    def remover (self, id):
        for professor in self.lista:
            if professor.id == id:
                self.lista.remove(professor)
                break
