# Author - João Pedro Podlasnisky dos Santos   
# Date - 08/set/2020
# Designed for Forum activity of Programming Language Class
#
# 
# Implement a list, do something and use a for to loop
# Personal library books list
#
# Lista é uma estrutura de dados do tipo sequencial que possui como principal característica ser mutável. 
# Ou seja, novos valores podem ser adicionados ou removidos da sequência. 
# Sabendo disso, desenvolva um código em Python, para um problema da sua escolha, 
# que possua lista como estrutura de dados e o for como estrutura de repetição.

livros = []
opcao = 1
opcoes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def cadastra_livro():
    global livros
    livro = input("Qual o livro que você deseja cadastrar?")
    livros.append(livro)


def remove_livro():
    global livros
    livro = input("Qual o livro que você deseja remover da lista?")
    if livro in livros:
        livros.remove(livro)
    else:
        print("Não consegui encontrar este livro na lista")


def remove_duplicados():
    r = []
    global livros
    for livro in livros:
        if livro not in r:
            r.append(livro) 
    livros = r
    

def ordena_crescente():
    global livros
    livros.sort()


def ordena_decrescente():
    global livros
    livros.sort(reverse=True)


def desfaz_ultima_insercao():
    global livros
    livros.pop()


def quantidade_de_itens():
    global livros
    print("Sua biblioteca já contém {} livros".format(len(livros)))


def listar_livros():
    global livros
    for livro in livros:
        print(livro)


def buscar_livro():
    global livros
    livro_buscado = input("Qual livro você quer verificar se está cadastrado? ")
    if livro_buscado in livros:
        print("Este livro já está cadastrado")
    else:
        cadastra_agora = input("Este livro ainda não foi cadastrado. Deseja cadastrar agora? Sim ou não?")
        if cadastra_agora.lower() == "sim":
            livros.append(livro_buscado)
        

        


while opcao != "0":
    # Menu
    print("*"*60)
    print("*** Esta é a lista de livros de sua biblioteca pessoal ***")
    print("*"*60)
    print("Suas opções são:")
    print("1 - Cadastrar livro")
    print("2 - Remover livro")
    print("3 - Remover livros duplicados")
    print("4 - Ordenar livros em ordem alfabética crescente")
    print("5 - Ordenar livros em ordem alfabética crescente")
    print("6 - Cancelar a última inserção")
    print("7 - Informar a quantidade de livros atual na biblioteca")
    print("8 - Listar todos os livros")
    print("9 - Verifica se livro já foi cadastrado")
    print("0 - SAIR")
    opcao = input("Qual opção você deseja?")

    # fim do menu
    if opcao in opcoes:
        if opcao == "1":
            cadastra_livro()
        elif opcao == "2":
            remove_livro()
        elif opcao == "3":
            remove_duplicados()
        elif opcao == "4":
            ordena_crescente()
        elif opcao == "5":
            ordena_decrescente()
        elif opcao == "6":
            desfaz_ultima_insercao()
        elif opcao == "7":
            quantidade_de_itens()
        elif opcao == "8":
            listar_livros()
        elif opcao == "9":
            buscar_livro()
        elif opcao == "0":
            print("Obrigado por usar o gerenciador de biblioteca pessoal")
    else:
        print("Opção inválida!")


