from pymongo import MongoClient
from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")

class ProductAnalyzer:
    def __init__(self, database: str):
        self.database = Database(database=database, collection="compras")
        self.client = MongoClient()
        self.db = self.client[database]
        self.collection = self.db["sales_collection"]
        
# 1 Retorne o total de vendas por dia
    def day_selling(self):
        result_day_sell = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$project": {"_id": 0, 
            "data_compra": {"$dateToString": {"format": "%Y-%m-%d", "date": {"$toDate": "$data_compra"}}},
            "valor": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}
            }},
            {"$group": {
            "_id": "$data_compra",
            "total_vendido_no_dia": {"$sum": "$valor"}}},
            {"$sort": {"_id": 1}}
    ])

        writeAJson(result_day_sell, "Total de vendas no dia")

# 2 Retorne o produto mais vendido em cada compra.
    def most_selling(self):
        result_most_sell = db.collection.aggregate([
            { "$unwind": "$produtos" },
            { "$group": { "_id": { "compra": "$_id", "produto": "$produtos.descricao" }, "total": { "$max": "$produtos.quantidade" } } },
            { "$sort": { "_id.compra": 1, "total": -1 } },
            { "$group": { "_id": "$_id.compra", "produto": { "$first": "$_id.produto" }, "total": { "$first": "$total" } } },
            { "$project": { "compra": "$_id", "produto": 1, "total": 1, "_id": 0 } }
    ])

        writeAJson(result_most_sell, "Produto mais vendido")

# 3 Encontrando o cliente que mais gastou em uma única compra.
    def customer_most(self):
        result_custom_most = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$_id", "cliente": {"$first": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        
        # chama a função writeAJson para gravar o resultado em um arquivo JSON
        writeAJson(result_custom_most, "Cliente que mais gastou em uma única compra")

# 4 Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
    def more_than_one(self):
        result_more_than = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 1}}},
        {"$project": {"_id": 0,"produto": "$produtos.descricao","quantidade_vendida": "$produtos.quantidade"}}
    ])

        writeAJson(result_more_than, "Produtos com quantidade vendida acima de 1 unidade")


# instancia a classe ProductAnalyzer e chama cada método para gerar o arquivo JSON
pa = ProductAnalyzer(database="mercado")
pa.day_selling()
pa.most_selling()
pa.customer_most()
pa.more_than_one()
