from database import Database
from championship_database import ChampionshipDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.235.55.237:7687", "neo4j", "basements-humidity-projects")
db.drop_all()

# Criando uma instância da classe ChampionshipDatabase para interagir com o banco de dados
championship_db = ChampionshipDatabase(db)

# Criando alguns campeonatos
championship_db.create_campeonato("Blast_2023")
championship_db.create_campeonato("Major_Varginha_2023")

# Criando alguns jogadores
championship_db.create_jogador("SK_Coldzera")
championship_db.create_jogador("SK_Fallen")
championship_db.create_jogador("SK_Fer")
championship_db.create_jogador("SK_Fnx")
championship_db.create_jogador("SK_Taco")
championship_db.create_jogador("SK_Dead")

championship_db.create_jogador("FNTC_Flusha")
championship_db.create_jogador("FNTC_JW")
championship_db.create_jogador("FNTC_Krimz")
championship_db.create_jogador("FNTC_Olofmeister")
championship_db.create_jogador("FNTC_Pronax")
championship_db.create_jogador("FNTC_Vuggo")

# Criando algumas partidas e suas relações com os campeonatos
championship_db.create_partida("SK_X_FNATIC", "Blast_2023")
championship_db.create_partida("FNATIC_X_SKG", "Major_Varginha_2023")

# Atualizando o nome de um campeonato
championship_db.update_campeonato("Blast_2023", "Blast_BH_2023")

championship_db.insert_jogador_partida("SK_Coldzera", "SK_X_FNATIC")
championship_db.insert_jogador_partida("SK_Coldzera", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("SK_Fallen", "SK_X_FNATIC")
championship_db.insert_jogador_partida("SK_Fallen", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("SK_Fer", "SK_X_FNATIC")
championship_db.insert_jogador_partida("SK_Fer", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("SK_Fnx", "SK_X_FNATIC")
championship_db.insert_jogador_partida("SK_Fnx", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("SK_Taco", "SK_X_FNATIC")
championship_db.insert_jogador_partida("SK_Taco", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("FNTC_Flusha", "SK_X_FNATIC")
championship_db.insert_jogador_partida("FNTC_Flusha", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("FNTC_JW", "SK_X_FNATIC")
championship_db.insert_jogador_partida("FNTC_JW", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("FNTC_Krimz", "SK_X_FNATIC")
championship_db.insert_jogador_partida("FNTC_Krimz", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("FNTC_Olofmeister", "SK_X_FNATIC")
championship_db.insert_jogador_partida("FNTC_Olofmeister", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("FNTC_Pronax", "SK_X_FNATIC")
championship_db.insert_jogador_partida("FNTC_Pronax", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("SK_Dead", "FNATIC_X_SKG")
championship_db.insert_jogador_partida("FNTC_Vuggo", "FNATIC_X_SKG")


championship_db.insert_campeonato_partida("Blast_BH_2023", "SK_X_FNATIC")
championship_db.insert_campeonato_partida("Major_Varginha_2023", "FNATIC_X_SKG")

# Deletando os técnicos
championship_db.delete_jogador("SK_Dead")
championship_db.delete_jogador("FNTC_Vuggo")

# Imprimindo todas as informações do banco de dados
print("Campeonatos:")
print(championship_db.get_campeonatos())
print("Jogadores:")
print(championship_db.get_jogadores())
print("Partidas:")
print(championship_db.get_partidas())

# Fechando a conexão com o banco de dados
db.close()