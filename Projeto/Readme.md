<h1 align="center"> Projeto Mongo DB Atlas + Python 💻 </h1>

- [Projeto](#o-projeto-)
- [Equipe](#equipe)
- [Guia de Instalação](#instalação-)
   - [Pré-requisitos](#pré-requisitos)
   - [Versão e atualização do PIP](#versão-e-atualização)
   - [Instalação do Pymongo e Gson](#instalando-o-pymongo-gson)
   - [Clone](#clonando-o-projeto)
- [Ativando a Venv](#ativando-a-venv-)  

# O Projeto 📈
Projeto da matéria de Laboratório de Banco de Dados II (C214), ministrada pelo monitor **Bruno Almeida**. Tem como objetivo demonstrar a utilização do mongo db atlas, junto com o python para criação de um
um sistema cujo intuito é administrar um projeto. O banco tem uma collection Projetos é possível administar as classes projeto, tarefa, equipe, membro. 

## Equipe
| ![Fernanda Nagata Ito](https://avatars.githubusercontent.com/u/99490194?v=4) | ![Igor Luiz Rodrigues](https://avatars.githubusercontent.com/u/89806466?s=400&u=e8107d3d169b3775f289e49470b097b45d778d68&v=4) |
| --- | --- |
| [Fernanda Nagata Ito](https://github.com/FerNagata) | [Igor Luiz Rodrigues](https://github.com/igu1nho) |


## Instalação ⚙💻

### Pré-requisitos
Para instalar o Pymongo e o Gson é necessário ter em sua máquina o Python instalado <a href="https://www.python.org/">python.org</a>

### ⚠️ Alguns IDE's como o <a href="https://www.jetbrains.com/pt-br/pycharm/">PyCharm</a> e o <a href="https://www.code.visualstudio.com/ ">VScode</a> já possuem o PIP integrado, ⚠️<br>

Abra um console com permissão de administrador no seu computador.
Após aberto, siga os seguintes passos:

### Versão e atualização
- Para verificar se instalou corretamente e saber sua versão, rode o seguinte comando:
```bash
pip --version
```

- Para atualizar sua versão do PIP, rode o seguinte comando:
```bash
python -m pip install --upgrade pip
```

### Instalando o PyMongo
- 1º Com um simples comando você já instala o PyMongo:
```bash
python -m pip install pymongo
```
### Instalando o Gson
- 2º Com um simples comando você já instala também o Gson:
```bash
python -m pip install gson
```

### Clonando o projeto
Agora é hora de baixar o projeto e poder testar.
- Com o terminal ainda aberto, navegue até a pasta onde deseja salvar o projeto e cole o seguinte comando:
```bash
git clone https://github.com/igu1nho/BD2/tree/main/Projeto
```

### Ativando a venv
- Cria virtual env chamada .venv
```
python -m venv .venv
```

- Ativa virtual env
```
$ .venv\Scripts\activate
```
