from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import googlemaps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presenca.db'

db = SQLAlchemy(app)

gmaps = googlemaps.Client(key='AIzaSyDSIZNte-JBAhTMCS_tKDyb2xZMGfGibl8')

class Presenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

@app.route('/', methods=['GET'])
def exibir_formulario():
    return render_template('form.html')

@app.route('/presenca', methods=['POST'])
def registrar_presenca():
    nome = request.form['nome']
    endereco = request.form['endereco']

    geocode_result = gmaps.geocode(endereco)

    if geocode_result:
        metric = geocode_result[0]['formatted_address']
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']

        presenca = Presenca(nome=nome, endereco=metric, latitude=latitude, longitude=longitude)
        db.session.add(presenca)
        db.session.commit()

        return jsonify({'message': 'Presença registrada com sucesso!'}), 201


if __name__ == '__main__':
    app.run()
