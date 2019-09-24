from tracemalloc import get_object_traceback

from flask import Flask, jsonify, request
from planetas_repository import PlanetasRepository
from models.planeta import Planeta
from bson.json_util import dumps
import json

app = Flask(__name__)


@app.route('/planetas', methods=['GET'])
def listar():
    planetas = dumps(repository.listar())
    return jsonify(planetas), 200


@app.route('/planeta/id/<string:id>', methods=['GET'])
def buscaPorId(id):
    planeta = dumps(repository.buscarPorId(id))
    return jsonify(planeta), 200


@app.route('/planeta/nome/<string:nome>', methods=['GET'])
def buscaPorNome(nome):
    planeta = dumps(repository.buscarPorNome(nome))
    return jsonify(planeta), 200


@app.route('/planeta/adicionar', methods=['POST'])
def inserirPlaneta():
    nome = request.get_json().get('nome')
    terreno = request.get_json().get('terreno')
    clima = request.get_json().get('clima')
    planeta = Planeta(nome,terreno,clima,0)
    repository.inserirPlaneta(planeta)
    return "", 201


@app.route('/planeta/remover', methods=['POST'])
def removerPlaneta():
    _id = request.get_json().get('_id')
    repository.removerPlaneta(_id)
    return "", 201


if __name__ == '__main__':
    repository = PlanetasRepository()
    novo_planeta = Planeta("Stewjon","Quente","Menor",0)
    repository.inserirPlaneta(novo_planeta)

    novo_planeta = Planeta("Terra", "Bom", "Medio", 0)
    repository.inserirPlaneta(novo_planeta)

    app.run(debug=False)