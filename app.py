from flask import Flask, render_template, request, redirect
from aluno_service import AlunoService
from professor_service import ProfessorService
from curso_service import CursoService

app = Flask(__name__)

aluno_service = AlunoService()
professor_service = ProfessorService()
curso_service = CursoService()

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
    aluno_service.adicionar(nome, matricula)
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
    aluno = aluno_service.buscar_por_id(id)
    return render_template("aluno/form.html", aluno=aluno)

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

    professor_service.adicionar(nome, cpf, disciplina)
    return redirect('/professor')

@app.route('/curso')
def listar_curso():
    lista = curso_service.listar()
    return render_template('curso/listar.html', lista=lista)

@app.route('/curso/form')
def novo_curso():
    return render_template("curso/form.html", curso=None)

@app.route("/curso/salvar/", methods=["POST"])
def salvar_curso():
    nivel = request.form.get("nivel")
    curso = request.form.get("curso")
    curso_service.adicionar(curso, nivel)
    return redirect('/curso')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True)
