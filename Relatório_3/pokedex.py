from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: str, collection: str):
        self.db = Database(database=database, collection=collection)
    
    def Pokemon_Name(self, name: str):
        query = {"name": name}
        result = self.db.collection.find(query)
        writeAJson(result, f"{name}_query")
        return result
    
    def Pokemon_Type(self, poke_type: str):
        query = {"type": poke_type}
        result = self.db.collection.find(query)
        writeAJson(result, f"{poke_type}_query")
        return result
    
    def Pokemon_Id(self, id: int):
        query = {"id": id}
        result = self.db.collection.find(query)
        writeAJson(result, f"id_{id}_query")
        return result

    def Pokemon_Weakness(self, weakness: str):
        query = {"weaknesses": weakness}
        result = self.db.collection.find(query)
        writeAJson(result, f"{weakness}_query")
        return result

    def Pokemon_Candy(self, candy: str):
        query = {"candy": candy}
        result = self.db.collection.find(query)
        writeAJson(result, f"{candy}_query")
        return result
    

pokedex = Pokedex(database="pokedex", collection="pokemons")

Pikachu = pokedex.Pokemon_Name("Pikachu")
Fire_types = pokedex.Pokemon_Type("Fire")
Id_mewtwo = pokedex.Pokemon_Id(150)
Ghost_weakness = pokedex.Pokemon_Weakness("Ghost")
Candy_especific = pokedex.Pokemon_Candy("Charmander Candy")