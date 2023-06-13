from projeto import Projeto
from equipe import Equipe
from membro import Membro
from tarefa import Tarefa

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print("-----------------------------------------------------")
            print("                       OPÇÕES")
            print("-----------------------------------------------------")
            print("1 - Criar projeto")
            print("2 - Adicionar membros")
            print("3 - Adicionar tarefa")
            print("4 - Ler projeto")
            print("5 - Atualizar projeto")
            print("6 - Atualizar tarefa")
            print("7 - Atualizar equipe")
            print("8 - Atualizar membro")
            print("9 - Deletar projeto")
            print("10 - Deletar tarefa")
            print("11 - Sair")
            print("-----------------------------------------------------")
            command = input("Digite sua opção: ")
            print("-----------------------------------------------------")
            if command == "11":
                print("Ate mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido. Tente novamente.")

class ProjetoCLI(SimpleCLI):
    def __init__(self, projeto_model):
        super().__init__()
        self.projeto_model = projeto_model
        self.add_command("1", self.criar_projeto)
        self.add_command("2", self.add_membros)
        self.add_command("3", self.add_tarefa)
        self.add_command("4", self.ler_projeto)
        self.add_command("5", self.atualizar_projeto)
        self.add_command("6", self.atualizar_tarefa)
        self.add_command("7", self.atualizar_equipe)
        self.add_command("8", self.atualizar_membro)
        self.add_command("9", self.deletar_projeto)
        self.add_command("10", self.deletar_tarefa)

    def criar_projeto(self):
        print("-- Informações do projeto")
        nome_projeto = input("Nome do projeto: ")
        status_projeto = input("Status do projeto: ")
        responsavel_projeto = input("Responsavel pelo projeto: ")
        print("\n-- Informações da primeira tarefa do Projeto: ")
        descricao_tarefa = input("Descricao da tarefa: ")
        data_inicio_tarefa = input("Data de inicio da tarefa: ")
        data_fim_tarefa = input("Data de termino da tarefa: ")
        status_tarefa = input("Status da tarefa: ")
        print("\n-- Informações da equipe responsável pela tarefa")
        id_equipe = input("ID da equipe: ")
        nome_equipe = input("Nome da equipe: ")
        print("\n-- Informações do Líder da Equipe")
        cpf_membro = input("CPF do membro: ")
        nome_membro = input("Nome do membro: ")

        projeto = Projeto(
            nome_projeto,
            status_projeto,
            responsavel_projeto,
            Tarefa(
                descricao_tarefa,
                data_inicio_tarefa,
                data_fim_tarefa,
                status_tarefa,
                Equipe(
                    id_equipe,
                    nome_equipe,
                    Membro(
                        cpf_membro,
                        nome_membro,
                        "True" # Está setado como True - pois é o líder da equipe
                    )
                )
            )
        )
        self.projeto_model.criarProjeto(projeto)

    def add_membros(self):
        id_projeto = input("ID do projeto: ")
        descricao_tarefa = input("Descrição da tarefa: ")
        cpf_membro = input("CPF do novo membro: ")
        nome_membro = input("Nome do novo membro: ")

        membro = Membro(cpf_membro, nome_membro, "False")
        self.projeto_model.addMembro(id_projeto, descricao_tarefa, membro)

    def add_tarefa(self):    
        id_projeto = input("ID do projeto: ")
        print("\n-- Informações da tarefa: ")
        descricao_tarefa = input("Descricao da tarefa: ")
        data_inicio_tarefa = input("Data de inicio da tarefa: ")
        data_fim_tarefa = input("Data de termino da tarefa: ")
        status_tarefa = input("Status da tarefa: ")
        print("\n-- Informações da equipe responsável pela tarefa")
        id_equipe = input("ID da equipe: ")
        nome_equipe = input("Nome da equipe: ")
        print("\n-- Informações do Líder da Equipe")
        cpf_membro = input("CPF do membro: ")
        nome_membro = input("Nome do membro: ")

        tarefa = Tarefa(
            descricao_tarefa,
            data_inicio_tarefa,
            data_fim_tarefa,
            status_tarefa,
            Equipe(
                id_equipe,
                nome_equipe,
                Membro(
                    cpf_membro,
                    nome_membro,
                    "True"
                )
            )
        )
        
        self.projeto_model.addTarefa(id_projeto, tarefa)

    def ler_projeto(self):
        id = input("Digite o ID do projeto: ")
        projeto_cursor = self.projeto_model.ler(id)

        print("-----------------------------------------------------")
        if projeto_cursor:
            for projeto in projeto_cursor:
                print(f"Nome do projeto: {projeto.get('nome', 'N/A')}")
                print(f"Status do projeto: {projeto.get('status', 'N/A')}")
                print(f"Responsável pelo projeto: {projeto.get('responsavel', 'N/A')}")

                for tarefa in projeto.get("tarefa", []):
                    print("-------------------------------")
                    print("Tarefa:")
                    print(f"  Descrição da tarefa: {tarefa.get('descricao', 'N/A')}")
                    print(f"  Data de início da tarefa: {tarefa.get('data_inicio', 'N/A')}")
                    print(f"  Data de término da tarefa: {tarefa.get('data_fim', 'N/A')}")
                    print(f"  Status da tarefa: {tarefa.get('status', 'N/A')}")
                    print("-------------------------------")

                    print("Equipe:")
                    equipe = tarefa.get("equipe", {})
                    print(f"  ID da equipe: {equipe.get('id', 'N/A')}")
                    print(f"  Nome da equipe: {equipe.get('nome', 'N/A')}")

                    print("-------------------------------")
                    print("Membro(s) da equipe:")
                    for membro in equipe.get("membros", []):
                        print(f"  CPF do membro: {membro.get('cpf', 'N/A')}")
                        print(f"  Nome do membro: {membro.get('nome', 'N/A')}")
                        print(f"  Líder da equipe: {membro.get('lider', 'N/A')}")
                        print("-----------------")
                    
        else:
            print("Projeto não encontrado.")

    def atualizar_projeto(self):
        id = input("Digite o id do projeto que deseja atualizar: ")
        nome_projeto = input("Nome do projeto: ")
        status_projeto = input("Status do projeto: ")
        responsavel_projeto = input("Responsavel pelo projeto: ")

        self.projeto_model.atualizarProjeto(id, nome_projeto, status_projeto, responsavel_projeto)

    def atualizar_tarefa(self):
        id_projeto = input("ID do projeto: ")
        descricao_tarefaVelha = input("Descrição da tarefa (atual): ")
        descricao_tarefaNova = input("Descrição da tarefa (nova): ")
        data_inicio_tarefa = input("Data de início da tarefa: ")
        data_fim_tarefa = input("Data de término da tarefa: ")
        status_tarefa = input("Status da tarefa: ")

        self.projeto_model.atualizarTarefa(id_projeto, descricao_tarefaVelha, descricao_tarefaNova, data_inicio_tarefa, data_fim_tarefa, status_tarefa)

    def atualizar_equipe(self):
        id_projeto = input("ID do projeto: ")
        descricao_tarefa = input("Descrição da tarefa: ")
        nome_equipe = input("Novo nome da equipe: ")

        self.projeto_model.atualizarEquipe(id_projeto, descricao_tarefa, nome_equipe)
    
    def atualizar_membro(self):
        id_projeto = input("ID do projeto: ")
        descricao_tarefa = input("Descrição da tarefa: ")
        cpf_busca = input("CPF de identificacao: ")
        cpf_membro = input("Novo CPF do membro: ")
        nome_membro = input("Nome do membro: ")
        lider_membro = input("Líder da equipe (True ou False): ")
        
        self.projeto_model.atualizarMembro(id_projeto, descricao_tarefa, cpf_busca, cpf_membro, nome_membro, lider_membro)


    def deletar_projeto(self):
        id = input("Digite o id: ")
        self.projeto_model.deletarProjeto(id)

    def deletar_tarefa(self):
        id = input("Digite o id: ")
        descricao = input("Digite a descrição da tarefa: ")
        self.projeto_model.deletarTarefa(id, descricao)    

    def run(self):
        print("\n------ Bem vindo ao Gerenciamento de Projetos! ------\n")
        super().run()