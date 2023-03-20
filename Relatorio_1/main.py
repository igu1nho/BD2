class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self):
        print(f"O professor {self.nome} está ministrando uma aula.")


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print(f"O aluno {self.nome} está presente.")


class Aula:
    def __init__(self, prof, assunto):
        self.prof = prof
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print(
            f"Presença na aula {self.assunto}, ministrada pelo professor {self.prof.nome}:"
        )
        for aluno in self.alunos:
            aluno.presenca()


professor = Professor("Bruno")
aluno1 = Aluno("Igor")
aluno2 = Aluno("Luiz")
aula = Aula(professor, "Banco de Dados II")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()
