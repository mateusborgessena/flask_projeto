class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Disciplina:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Historico:
    def __init__(self, aluno):
        self.aluno = aluno
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def calcular_media(self):
        if not self.disciplinas:
            return 0
        soma = sum(d.nota for d in self.disciplinas)
        return soma / len(self.disciplinas)

    def resumo(self):
        print("\n--- HISTÓRICO ESCOLAR ---")
        print(f"Aluno: {self.aluno.nome}")
        print(f"Matrícula: {self.aluno.matricula}")
        print("Disciplinas:")
        for d in self.disciplinas:
            print(f"- {d.nome} | Nota: {d.nota}")

        media = self.calcular_media()
        print(f"Média do período: {media:.2f}")


aluno1 = Aluno("João da Silva", "20231234")

historico = Historico(aluno1)

disciplina1 = Disciplina("Matemática", 8.0)
disciplina2 = Disciplina("Português", 7.5)

historico.adicionar_disciplina(disciplina1)
historico.adicionar_disciplina(disciplina2)

historico.resumo()


