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
        self._validar_dados(nome, matricula)
        id = self.proximo_id
        aluno = Aluno( id, nome , matricula)
        self.lista.append(aluno)
        self.proximo_id +=1



    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for aluno in self.lista:
            if aluno.id == id:   
                return aluno    
        return None 
    
    def atualizar(self,id,nome,matricula):
        self._validar_dados(nome,matricula,id)
        aluno = self.buscar_por_id(id)
        if aluno:
            aluno.nome = nome
            aluno.matricula = matricula

    def _validar_dados(self, nome, matricula, id=None):
        if not nome or not matricula:
            raise Exception("Nome e matrícula são obrigatórios")
        for aluno in self.lista:
            if aluno.matricula == matricula:
                if id is None or aluno.id != id:
                    raise Exception("Matrícula já existe")


    def remover (self, id):
        for aluno in self.lista:
            if aluno.id == id:
                self.lista.remove(aluno)
                break
            
    

        

