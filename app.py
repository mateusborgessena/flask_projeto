from flask import Flask, render_template
from alunos_service import AlunoService
from professor_service import ProfessorService

app = Flask(__name__)

aluno_service = AlunoService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/aluno')
def listar_aluno():
    listar = aluno_service.listar()
    return render_template('aluno/listar.html', lista=lista)

@app.route('/professor')
def listar_professor():
    listar = professor_service.listar()
    return render_template('professor/listar.html', lista=lista)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True)
