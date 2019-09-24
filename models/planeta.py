from bson.objectid import ObjectId

class Planeta:
    def __init__(self, nome, clima, terreno, quantidade_filmes):
        self. nome = nome
        self.clima = clima
        self.terreno = terreno
        self.quantidade_filmes = quantidade_filmes

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getClima(self):
        return self.clima

    def getTerreno(self):
        return self.terreno

    def getQuantidadeFilmes(self):
        return self.quantidade_filmes

    def setNome(self, nome):
        self.nome = nome

    def setClima(self, clima):
        self.clima = clima

    def setTerreno(self, terreno):
        self.terreno = terreno

    def setQuantidadeFilmes(self, quantidade_filmes):
        self.quantidade_filmes = quantidade_filmes

    @staticmethod
    def construir_do_json(dados_json):
        if dados_json is not None:
            try:
                return Planeta(dados_json.get('_id', None),
                    dados_json['nome'],
                    dados_json['terreno'],
                    dados_json['clima'])
            except KeyError as e:
                raise Exception("Key not found in json_data: {}".format(e.message))
        else:
            raise Exception("Nenhum dado criado!")