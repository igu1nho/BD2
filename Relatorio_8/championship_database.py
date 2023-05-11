
class ChampionshipDatabase:
    def __init__(self, database):
        self.db = database

    def create_campeonato(self, name):
        query = "CREATE (:Campeonato {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_jogador(self, name):
        query = "CREATE (:Jogador {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_partida(self, name, campeonato_name):
        query = "MATCH (c:Campeonato {name: $campeonato_name}) CREATE (:Partida {name: $name})<-[:TEM_UMA]-(c)"
        parameters = {"name": name, "campeonato_name": campeonato_name}
        self.db.execute_query(query, parameters)

    def get_campeonatos(self):
        query = "MATCH (c:Campeonato) RETURN c.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_jogadores(self):
        query = "MATCH (j:Jogador) RETURN j.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_partidas(self):
        query = "MATCH (p:Partida)<-[:TEM_UMA]-(c:Campeonato) RETURN p.name AS name, c.name AS campeonato_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["campeonato_name"]) for result in results]

    def update_campeonato(self, old_name, new_name):
        query = "MATCH (c:Campeonato {name: $old_name}) SET c.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_jogador_partida(self, jogador_name, partida_name):
        query = "MATCH (j:Jogador {name: $jogador_name}) MATCH (p:Partida {name: $partida_name}) CREATE (j)-[:JOGA_A]->(p)"
        parameters = {"jogador_name": jogador_name, "partida_name": partida_name}
        self.db.execute_query(query, parameters)
    
    def insert_campeonato_partida(self, campeonato_name, partida_name):
        query = "MATCH (c:Campeonato {name: $campeonato_name}) MATCH (p:Partida {name: $partida_name}) CREATE (c)-[:TEM_UMA]->(p)"
        parameters = {"campeonato_name": campeonato_name, "partida_name": partida_name}
        self.db.execute_query(query, parameters)

    def delete_campeonato(self, name):
        query = "MATCH (c:Campeonato {name: $name}) DETACH DELETE c"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_jogador(self, name):
        query = "MATCH (j:Jogador {name: $name}) DETACH DELETE j"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_partida(self, name):
        query = "MATCH (p:Partida {name: $name})<-[:TEM_UMA]-(c:Campeonato) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)