from equipe import Equipe

class Tarefa:
    def __init__(self, descricao,  dataInicio, dataFim, status, equipe:Equipe):
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.status = status
        self.equipe = equipe
