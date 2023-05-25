from teacher_crud import TeacherCRUD

class CLI:
    def __init__(self):
        self.teacher_crud = TeacherCRUD()

    def start(self):
        while True:
            print("1. Criar professor")
            print("2. Pesquisar professor")
            print("3. Atualizar o CPF do professor")
            print("4. Deletar o professor")
            print("0. Sair")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.create_teacher()
            elif choice == '2':
                self.show_teacher()
            elif choice == '3':
                self.update_cpf()
            elif choice == '4':
                self.delete_teacher()
            elif choice == '0':
                self.teacher_crud.db.close()
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def create_teacher(self):
        name = input("Digite o nome do professor: ")
        ano_nasc = int(input("Digite o ano de nascimento do professor: "))
        cpf = input("Digite o CPF do professor: ")

        self.teacher_crud.create(name, ano_nasc, cpf)

    def show_teacher(self):
        name = input("Digite o nome do professor: ")

        self.teacher_crud.read(name)

    def update_cpf(self):
        name = input("Digite o nome do professor: ")
        new_cpf = input("Digite o novo CPF do professor: ")

        self.teacher_crud.update(name, new_cpf)

    def delete_teacher(self):
        name = input("Digite o nome do professor a ser deletado: ")

        self.teacher_crud.delete(name)


cli = CLI()
cli.start()

'''
# b) Digitar os comandos abaixo para criar o professor Chris
1) clique na opção 1
2) Digite:
name: Chris Lima
ano_nasc: 1956
cpf: 189.052.396-66

# c)
1) Opção 2
2) Digite:
Chris Lima

# d)
1) Opção 3
2) Digite:
Chris Lima
162.052.777-77

'''
