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

    def adicionar(self, nome, cpf, disciplina):
        self._validar_dados(nome, cpf,disciplina)
        id = self.proximo_id
        professor = Professor( id, nome , cpf, disciplina)
        self.lista.append(professor)
        self.proximo_id +=1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for professor in self.lista:
            if professor.id == id:   
                return professor    
        return None 

    def atualizar(self,id,nome,cpf,disciplina ):
        self._validar_dados(nome, cpf, disciplina, id)
        professor = self.buscar_por_id(id)
        if professor:
            professor.nome = nome
            professor.cpf = cpf
            professor.disciplina = disciplina
    
    def _validar_dados(self, nome, cpf, id=None):
        if not nome or not cpf:
            raise Exception("Nome e CPF são obrigatórios")
        for professor in self.lista:
            if professor.cpf == cpf:
                if id is None or professor.id != id:
                    raise Exception("CPF já existe")

    def remover (self, id):
        for professor in self.lista:
            if professor.id == id:
                self.lista.remove(professor)
                break
