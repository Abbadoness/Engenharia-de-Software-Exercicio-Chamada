from flask import Flask, render_template, request
import twitter

app = Flask(__name__)

aluno1 = ["Alecio Oliveira Gotti",'a1']
aluno2 = ["Alyson Marques Gomes",'a2']
aluno3 = ["Amanda de Almeida Passos",'a3']
aluno4 = ["Ana Flavia Cezario de Oliveira",'a4']
aluno5 = ["Ana Julia Candido Pereira",'a5']

@app.route("/", methods=["GET", "POST"])
def main():
    
    if request.args.get('a1', None):
        aluno1[1] = process_text(request.args['a1'])
    
    if request.args.get('a2', None):
        aluno2[1] = process_text(request.args['a2'])
        
    if request.args.get('a3', None):
        aluno3[1] = process_text(request.args['a3'])
            
    if request.args.get('a4', None):
        aluno4[1] = process_text(request.args['a4'])
            
    if request.args.get('a5', None):
        aluno5[1] = process_text(request.args['a5'])
        
    alunos = [aluno1,aluno2,aluno3,aluno4,aluno5]

    return render_template('index.html', alunos=alunos)

def process_text(text):
    return "FOO" + text
    
class Twitter():
    def __init__(self):
        self.api = twitter.Api(consumer_key='B9Vr3WkqtarTKQBUbiTUJHtKa', consumer_secret='LfO7ZlIqUqbjyIKm6xSCyL1aQRstWWdPJTt4MwUIVj5TiRCHtM', access_token_key='1652051666621853697-XlUJyqmGddKWb7R0p0GTSxvsKZKc3G', access_token_secret='xigBLcL5l7Y1RHbJ3Roft6PON7uawNxVwRDiMCv0baLhn')
    
    def post_msg(self):
        response = self.api.PostUpdate(app.aluno1[0]+'-'+app.aluno1[1]+'/n'+app.aluno2[0]+'-'+app.aluno2[1]+'/n'+app.aluno3[0]+'-'+app.aluno3[1]+'/n'+app.aluno4[0]+'-'+app.aluno4[1]+'/n'+app.aluno5[0]+'-'+app.aluno5[1]+'/n')


if __name__ == '__main__':
    app.run(debug= True)
    t = Twitter()
    t.post_msg()