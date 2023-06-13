from projeto import ProjetoDAO
from cli import ProjetoCLI

projetoDAO = ProjetoDAO()

projetocli = ProjetoCLI(projetoDAO)
projetocli.run()