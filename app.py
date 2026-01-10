from flask import Flask, render_template, request, redirect
from aluno_service import AlunoService, Aluno
from professor_service import ProfessorService, Professor
from curso_service import CursoService, Curso
from disciplina_service import DisciplinaService, Disciplina






app = Flask(__name__)

aluno_service = AlunoService()
professor_service = ProfessorService()
curso_service = CursoService()
disciplina_service = DisciplinaService()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/aluno')
def listar_aluno():
    lista = aluno_service.listar()
    return render_template('aluno/listar.html', lista=lista)

@app.route('/aluno/form')
def novo_aluno():
    return render_template("aluno/form.html", aluno=None)

@app.route("/aluno/salvar/", methods=["POST"])
def salvar_aluno():
    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    try:
        aluno_service.adicionar(nome, matricula,)
    except  Exception as e:
        aluno = Aluno('',nome,matricula)
        return render_template("aluno/form.html",aluno=aluno, erro=str(e))
    
    return redirect('/aluno')

@app.route("/aluno/editar/<int:id>")
def editar_aluno(id):
    aluno = aluno_service.buscar_por_id(id)
    return render_template("aluno/form.html", aluno=aluno)

@app.route("/aluno/salvar/<int:id>", methods=["POST"])
def atualizar_aluno(id):
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    aluno_service.atualizar(id, nome, matricula)
    return redirect('/aluno')

@app.route("/aluno/remover/<int:id>")
def remover_aluno(id):
    aluno_service.remover(id)
    return redirect("/aluno")

@app.route('/professor')
def listar_professor():
    lista = professor_service.listar()
    return render_template('professor/listar.html', lista=lista)

@app.route('/professor/form')
def novo_professor():
    return render_template("professor/form.html", professor=None)

@app.route("/professor/salvar/", methods=["POST"])
def salvar_professor():
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    disciplina = request.form.get("disciplina")
    try:
        professor_service.adicionar(nome, cpf, disciplina)
    except  Exception as e:
        professor = Professor('',nome,cpf, disciplina)
        return render_template("professor/form.html",professor=professor, erro=str(e))
   
    return redirect('/professor')

@app.route("/professor/editar/<int:id>")
def editar_professor(id):
    professor = professor_service.buscar_por_id(id)
    return render_template("/professor/form.html",professor=professor)

@app.route("/professor/salvar/<int:id>", methods=["POST"])
def atualizar_professor(id):
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    disciplina = request.form["disciplina"]
    professor_service.atualizar(id, nome, cpf, disciplina)
    return redirect('/professor')

@app.route("/professor/remover/<int:id>")
def remover_professor(id):
    professor_service.remover(id)
    return redirect("/professor")

@app.route('/curso')
def listar_cursos():
    lista = curso_service.listar()
    return render_template('curso/listar.html', lista=lista)

@app.route('/curso/form')
def novo_curso():
    return render_template("curso/form.html", curso=None)

@app.route("/curso/salvar/", methods=["POST"])
def salvar_curso():
    nome = request.form.get("nome")
    nivel = request.form.get("nivel")
    try:
        curso_service.adicionar(nome, nivel)
    except  Exception as e:
        curso = Curso('',nome,nivel)
        return render_template("curso/form.html",curso=curso, erro=str(e))
    return redirect("/curso")

@app.route("/curso/editar/<int:id>")
def editar_curso(id):
    curso = curso_service.atualizar(id)
    return render_template("/curso/form.html", curso=curso)

@app.route("/curso/salvar/<int:id>", methods=["POST"])
def atualizar_curso(id):
    nivel = request.form["nivel"]
    nome = request.form["nome"]
    curso_service.atualizar(id, nivel, nome)
    return redirect('/curso')

@app.route("/curso/remover/<int:id>")
def remover_curso(id):
    curso_service.remover(id)
    return redirect ("/curso")

@app.route('/disciplina')
def listar_disciplina():
    lista = disciplina_service.listar()
    return render_template('disciplina/listar.html', lista=lista)

@app.route('/disciplina/form')
def nova_disciplina():
    return render_template("disciplina/form.html", disciplina=None)

@app.route("/disciplina/salvar/", methods=["POST"])
def salvar_disciplina():
    nome = request.form.get("nome")
    carga_horaria = request.form.get("carga_horaria")
    ementa = request.form.get("ementa")
    try:
        disciplina_service.adicionar(nome, carga_horaria,ementa )
    except  Exception as e:
        disciplina = Disciplina('',nome,carga_horaria, ementa)
        return render_template("disciplina/form.html",disciplina=disciplina, erro=str(e))

@app.route("/disciplina/editar/<int:id>")
def editar_disciplina(id):
    disciplina_service.buscar_por_id(id)
    return redirect("/disciplina")

@app.route("/disciplina/remover/<int:id>")
def remover_disciplina(id):
    disciplina_service.remover(id)
    return render_template("/disciplina")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True)
