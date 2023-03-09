from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

pokemon = db.collection.find({"name": "Bulbasaur"})

writeAJson(pokemon, "pokemon")