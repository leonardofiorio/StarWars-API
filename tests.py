from planetas_repository import PlanetasRepository
from bson.objectid import ObjectId
from models.planeta import Planeta
import json

repository = PlanetasRepository()

class TestPlanetasRepository:

    def test_busca_por_nome(self):
        retorno = repository.buscarPorNome("Stewjon")
        assert retorno['nome'] == "Stewjon"
        assert retorno['terreno'] == "Menor"
        assert retorno['clima'] == 'Quente'
        assert retorno['quantidade_filmes'] == 0


    def test_buscar_por_id(self):
        retorno_por_nome = repository.buscarPorNome("Stewjon")
        id = retorno_por_nome['_id']

        retorno_por_id = repository.buscarPorId(id)
        assert retorno_por_id['_id'] == retorno_por_nome['_id']
        assert retorno_por_id['nome'] == retorno_por_nome['nome']
        assert retorno_por_id['terreno'] == retorno_por_nome['terreno']
        assert retorno_por_id['clima'] == retorno_por_nome['clima']
        assert retorno_por_id['quantidade_filmes'] == retorno_por_nome['quantidade_filmes']


    def test_inserir_planeta(self):
        planeta = Planeta("Polis Massa", "artificial temperate ", "airless asteroid", 0)
        repository.inserirPlaneta(planeta)
        retorno = repository.buscarPorNome("Polis Massa")
        assert retorno['nome'] == "Polis Massa"
        assert retorno['terreno'] == "airless asteroid"
        assert retorno['clima'] == 'artificial temperate '
        assert retorno['quantidade_filmes'] == 1


    def test_remover_planeta(self):
        retorno = repository.buscarPorNome("Terra")
        id = retorno['_id']

        repository.removerPlaneta(ObjectId(id))

        assert repository.buscarPorNome("Terra") == None