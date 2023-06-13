from membro import Membro
from typing import List

class Equipe:
    def __init__(self,id, nome, membros:List[Membro]):
        self.id = id
        self.nome = nome
        self.membros = membros