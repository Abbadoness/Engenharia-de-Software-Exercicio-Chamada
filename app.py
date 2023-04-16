from flask import Flask, render_template, request

app = Flask(__name__)

"""class Aluno:
    def __init__(self, id,nome, presença):
        self.id = id
        self.nome = nome
        self.presença = presença
"""

aluno1 = ["Alecio Oliveira Gotti",'a1']
aluno2 = ["Alyson Marques Gomes",'a2']
aluno3 = ["Amanda de Almeida Passos",'a3']
aluno4 = ["Ana Flavia Cezario de Oliveira",'a4']
aluno5 = ["Ana Julia Candido Pereira",'a5']

@app.route("/")
def main():
    aluno1[1] = request.args.get('a1')
    aluno2[1] = request.args.get('a2')
    aluno3[1] = request.args.get('a3')
    aluno4[1] = request.args.get('a4')
    aluno5[1] = request.args.get('a5')

    alunos = [aluno1,aluno2,aluno3,aluno4,aluno5]

    return render_template('index.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug= True)