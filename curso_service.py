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

    def adicionar(self, nome, nivel):
        id = self.proximo_id
        novo_curso = Curso(id, nivel, nome)
        self.lista.append(novo_curso)
        self.proximo_id += 1

    def listar(self):
        return self.lista
