from neo4j import GraphDatabase

# Função que faz uma consulta no banco de dados Neo4j
def run_query(query):
    driver = GraphDatabase.driver("bolt://18.215.15.78:7687", auth=("neo4j", "misfits-claw-assistants"))
    with driver.session() as session:
        result = session.run(query)
        records = list(result)  # Converte o resultado em uma lista
        result.consume()  # Consumir todos os registros
        return records

# Funcao que fara as buscas para cada uma das perguntas
def main():
# 1)
    # a)
    query_renzo = "MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
    resultado_renzo = run_query(query_renzo)
    renzo = [(record["ano_nasc"], record["cpf"]) for record in resultado_renzo]
    print("Dados do Professor Renzo:")
    print(renzo)

    # b)
    query_prof_m = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
    resultado_prof_m = run_query(query_prof_m)
    prof_m = [(record["name"], record["cpf"]) for record in resultado_prof_m]
    print("Professores quem o nome começa com a letra 'M':")
    print(prof_m)

    # c)
    query_cidades = "MATCH (c:City) RETURN c.name AS cidade"
    resultado_cidade = run_query(query_cidades)
    cidades = [record["cidade"] for record in resultado_cidade]
    print("Cidades encontradas:")
    print(cidades)

    # d)
    query_escolas = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS nome_escola, s.address AS endereco, s.number AS numero"
    resultado_escola = run_query(query_escolas)
    escolas = [(record['nome_escola'], record['endereco'], record['numero']) for record in resultado_escola]
    print("Escolas:")
    print(escolas)

# 2)
    # a)
    query_prof_ano = "MATCH (t:Teacher) RETURN max(t.ano_nasc) AS mais_jovem, min(t.ano_nasc) AS mais_velho"
    result_prof_ano = run_query(query_prof_ano)
    mais_jovem = result_prof_ano[0]["mais_jovem"]
    mais_velho = result_prof_ano[0]["mais_velho"]
    print("Professor mais jovem:", mais_jovem, " e o professor mais velho:", mais_velho)

    # b)
    query_media = "MATCH (c:City) RETURN avg(c.population) AS media_populacao"
    resultado_media = run_query(query_media)
    media_populacao = resultado_media[0]["media_populacao"]
    print("Média de população das cidades cadastradas:", media_populacao)

    # c)
    query_cep = "MATCH (c:City {cep: '37540-000'}) RETURN replace(c.name, 'a', 'A') AS nome_modificado"
    resultado_cep = run_query(query_cep)
    nome_A = resultado_cep[0]["nome_modificado"]
    print("Nome da cidade com 'A':", nome_A)

    # d)
    query_c = "MATCH (t:Teacher) RETURN t.name AS nome_professor, substring(t.name, 2, 1) AS terceira_letra"
    resultado_c = run_query(query_c)
    for record in resultado_c:
        nome_professor = record["nome_professor"]
        terceira_letra = record["terceira_letra"]
        print("Professor:", nome_professor)
        print("3ª letra do nome:", terceira_letra)
        print()

if __name__ == "__main__":
    main()