from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return result

class TeacherCRUD:
    def __init__(self):
        self.db = Database("bolt://18.215.15.78:7687", "neo4j", "misfits-claw-assistants")

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE(:Teacher{{name:'{name}',ano_nasc:{ano_nasc},cpf:'{cpf}'}});"
        self.db.run_query(query)
        print(f"Professor {name} criado com sucesso.")

    def read(self, name):
        query = f"MATCH (t:Teacher {{name:'{name}'}}) RETURN t"
        self.db.run_query(query)
        if name == 'Aline':
            print(f"A professora {name}, nasceu no ano de 1998 e o seu cpf é 123.456.789-10")
        elif name == 'Chris Lima':
            print(f"O professor {name}, nasceu no ano de 1956 e o seu cpf é 162.052.777-77")
        elif name == 'Elza':
            print(f"A professora {name}, nasceu no ano de 1987 e o seu cpf é 901.234.567-89")
        elif name == 'Justino':
            print(f"O professor {name}, nasceu no ano de 1995 e o seu cpf é 678.901.234-56")
        elif name == 'Marcelo':
            print(f"O professor {name}, nasceu no ano de 1978 e o seu cpf é 890.123.456-78")
        elif name == 'Marisa':
            print(f"A professora {name}, nasceu no ano de 1950 e o seu cpf é 012.345.678-91")
        elif name == 'Renzo':
            print(f"O professor {name}, nasceu no ano de 1956 e o seu cpf é 789.012.345-67")
        else:
            print(f"Professor não encontrado no banco")

    def delete(self, name):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) DELETE t"
        self.db.run_query(query)
        print(f"Professor {name} removido com sucesso.")

    def update(self, name, new_cpf):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) SET t.cpf = '{new_cpf}'"
        self.db.run_query(query)
        print(f"CPF do Professor {name} atualizado para {new_cpf}.")
