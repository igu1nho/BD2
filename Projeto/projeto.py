from database import Database
from bson.objectid import ObjectId
from tarefa import Tarefa
from membro import Membro

class Projeto: 
    def __init__(self, nome, status, responsavel, tarefa:Tarefa):
        self.nome = nome
        self.status = status
        self.responsavel = responsavel
        self.tarefa = tarefa

class ProjetoDAO:
    def __init__(self):
        self.db = Database(database="gerenciamento", collection="Projeto")
    def criarProjeto(self, projeto:Projeto):
        try:
            res = self.db.collection.insert_one({
                "nome": projeto.nome,
                "status": projeto.status,
                "responsavel": projeto.responsavel,
                "tarefa": [{
                    "descricao": projeto.tarefa.descricao,
                    "data_inicio": projeto.tarefa.dataInicio,
                    "data_fim": projeto.tarefa.dataFim,
                    "status": projeto.tarefa.status,
                    "equipe": {
                        "id": projeto.tarefa.equipe.id,
                        "nome": projeto.tarefa.equipe.nome,
                        "membros": [{
                            "cpf": projeto.tarefa.equipe.membros.cpf,
                            "nome": projeto.tarefa.equipe.membros.nome,
                            "lider": projeto.tarefa.equipe.membros.lider
                            }]
                        } 
                    }]
                })
            print(f"Projeto criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Houve um erro ao tentar criar um projeto: {e}")
            return None
        
    def addMembro(self, id:str, descricao, membro:Membro):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id),
                                                 "tarefa": {
                                                    "$elemMatch": {
                                                        "descricao": descricao
                                                    }
                                                }},{"$push":
                                                        {"tarefa.$.equipe.membros":{
                                                            "cpf": membro.cpf,
                                                            "nome": membro.nome,
                                                            "lider": membro.lider
                                                        }}})
            print(f"Membro adicionado!")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar adicionar um projeto: {e}")
            return None
        
    def addTarefa(self, id:str, tarefa:Tarefa):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)},
                                                {"$push":
                                        {"tarefa": {
                                            "descricao": tarefa.descricao,
                                            "data_inicio": tarefa.dataInicio,
                                            "data_fim": tarefa.dataFim,
                                            "status": tarefa.status,
                                                "equipe": {
                                                    "id":tarefa.equipe.id,
                                                    "nome": tarefa.equipe.nome,
                                                    "membros": [{
                                                        "cpf": tarefa.equipe.membros.cpf,
                                                        "nome": tarefa.equipe.membros.nome,
                                                        "lider": tarefa.equipe.membros.lider
                                                        }]
                                                    } 
                                        }}
                })
            print(f"Tarefa adicionada!")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar adicionar um projeto: {e}")
            return None

    def ler(self, id: str):
        try:
            res = self.db.collection.find({"_id": ObjectId(id)})
            return res
        except Exception as e:
            print(f"Houve um erro ao tentar ler o projeto: {e}")
            return None

    def atualizarProjeto(self, id: str, nome, status, responsavel): 
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome, 
                                                                                 "status": status,
                                                                                 "responsavel": responsavel}})
            print(f"Projeto atualizado: {res.modified_count} documento(s) modificado")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar atualizar o projeto: {e}")
            return None
        
    def atualizarTarefa(self,id, descricaoVelha, descricaoNova, dataInicio, dataFim, status): 
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id),
                                                 "tarefa": {
                                                    "$elemMatch": {
                                                        "descricao": descricaoVelha
                                                    }
                                                }},{"$set":{"tarefa.$.descricao": descricaoNova,
                                                            "tarefa.$.data_inicio": dataInicio,
                                                            "tarefa.$.data_fim": dataFim,
                                                            "tarefa.$.status": status}})

            print(f"Tarefa atualizada: {res.modified_count} documento(s) modificado")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar atualizar o projeto: {e}")
            return None
        
    def atualizarEquipe(self, id: str, descricao_tarefa, nome): 
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id), "tarefa": {
                                                    "$elemMatch": {
                                                        "descricao": descricao_tarefa
                                                    }
                                                }}, {"$set": {"tarefa.$.equipe.nome": nome}})
            print(f"Equipe atualizado: {res.modified_count} documento(s) modificado")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar atualizar o projeto: {e}")
            return None
        
    def atualizarMembro(self, id, descricao_tarefa, cpf_busca, cpf_membro, nome_membro, lider_membro): 
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id), "tarefa.descricao": descricao_tarefa, "tarefa.equipe.membros": {
                                                    "$elemMatch":{
                                                        "cpf":cpf_busca
                                                    }
                                                }}, {"$set": {"tarefa.$[tarefa].equipe.membros.$.cpf": cpf_membro,
                                                              "tarefa.$[tarefa].equipe.membros.$.nome": nome_membro,
                                                              "tarefa.$[tarefa].equipe.membros.$.lider": lider_membro
                                                }},array_filters=[
                                                    {"tarefa.descricao": descricao_tarefa}])
            
            print(f"Responsável atualizado: {res.modified_count} documento(s) modificado")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar atualizar o projeto: {e}")
            return None
    
    def deletarProjeto(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Projeto deletado: {res.deleted_count} documento(s) deletado")
            return res.deleted_count
        except Exception as e:
            print(f"Houve um erro ao tentar deletar o projeto: {e}")
            return None
        
    def deletarTarefa(self, id: str, descricao_tarefa): #obs: não estamos usando a função delete_one, mas sim a função update_one, pois estamos modificando um documento
        try:
            res = self.db.collection.update_one({ "_id": ObjectId(id) }, { "$pull": { "tarefa": { "descricao": descricao_tarefa }}})
            print(f"Projeto deletado: {res.modified_count} documento(s) deletado")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar deletar o projeto: {e}")
            return None
        
