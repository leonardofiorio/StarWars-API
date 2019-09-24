from models.planeta import Planeta
import pymongo
from bson.objectid import ObjectId
import requests
import json


class PlanetasRepository(object):

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["starwars"]
        self.mycol = self.mydb["planetas"]


    def buscarPorId(self, planeta_id):
        if planeta_id is None:
            return self.mycol.find_one({})
        else:
            return self.mycol.find_one({"_id": ObjectId(planeta_id)})


    def listar(self):
        return self.mycol.find()


    def buscarPorNome(self, planeta_nome):
        if planeta_nome is None:
            return self.mycol.find_one({})
        else:
            return self.mycol.find_one({"nome": planeta_nome})


    def inserirPlaneta(self, planeta):
        r = requests.get('https://swapi.co/api/planets/')
        dicionario = json.loads(r.text)
        quantidade_total = dicionario['count']
        qtd_max_pag = 10
        resultados = dicionario['results']
        encontrou = False

        if quantidade_total < qtd_max_pag:
            # Para caso a quantidade total resultados for menor que a quantidade pre-definida por pagina
            for j in range(0, quantidade_total):
                if resultados[j]['name'] == planeta.getNome():
                    planeta.setQuantidadeFilmes(len(resultados[j]['films']))
                    encontrou = True
        else:
            # Para as paginas com quantidade cheia
            quantidade_paginas = quantidade_total // qtd_max_pag

            print("Quantidade paginas " + str(quantidade_paginas))
            print("Quantidade total " + str(quantidade_total))
            print("Quantidade maxima por pagina " + str(qtd_max_pag))

            for i in range(1 , quantidade_paginas):
                for j in range(0, qtd_max_pag):
                    print(str(i) + " " + str(j) + " " + resultados[j]['name'])
                    if (resultados[j]['name'] == planeta.getNome()):
                        planeta.setQuantidadeFilmes(len(resultados[j]['films']))
                        encontrou = True

                r = requests.get('https://swapi.co/api/planets/?page=' + str(i))
                dicionario = json.loads(r.text)
                resultados = dicionario['results']

            # Para caso a ultima pagina nao esteja totalmente preenchida
            resto = quantidade_total % qtd_max_pag
            print("Resto " + str(resto))
            if not(encontrou) and (resto != 0):
                for j in range(0, resto):
                    if (resultados[j]['name'] == planeta.getNome()):
                        planeta.setQuantidadeFilmes(len(resultados[j]['films']))
                        encontrou = True

        planeta = {'nome': planeta.getNome(), 'terreno': planeta.getTerreno(), 'clima': planeta.getClima(),
                   'quantidade_filmes': planeta.getQuantidadeFilmes()}
        return self.mycol.insert_one(planeta)


    def removerPlaneta(self, id):
        if id is not None:
            return self.mycol.delete_one({"_id": ObjectId(id)})
        else:
            raise Exception("Nada foi removido")