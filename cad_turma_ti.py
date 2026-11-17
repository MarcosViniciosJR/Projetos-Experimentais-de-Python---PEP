#Teste de Codigo com Menu"
print("="*99)

print("\n  CADASTRO DE ALUNOS DA TURMA DE TI  \n")
print("-"*99)
lista_alunos = [
    ["Lucas", 22, "Sistemas de Informação", [8.5, 7.0, 9.2]],
    ["Ana Beatriz", 24, "Ciência da Computação", [9.2, 8.8, 9.5]],
    ["João Pedro", 31, "Engenharia de Software", [7.8, 6.5, 8.0]],
    ["Fernanda Rocha", 25, "Ciência da Computação", [8.9, 9.0, 8.4]],
    ["Maria Eduarda", 19, "Análise e Desenvolvimento de Sistemas", [9.5, 9.1, 9.8]],
    ["Gabriel", 42, "Ciência da Computação", [6.8, 7.2, 7.0]],
    ["Larissa Lima", 26, "Engenharia de Software", [8.1, 8.5, 7.9]],
    ["Carlos Eduardo", 35, "Sistemas de Informação", [7.4, 7.0, 8.1]],
    ["Rafael", 30, "Análise e Desenvolvimento de Sistemas", [8.3, 8.0, 8.7]],
    ["Juliana Costa", 28, "Análise e Desenvolvimento de Sistemas", [9.0, 8.5, 9.2]],
    ["Mariana Santos", 23, "Sistemas de Informação", [7.9, 8.2, 7.5]],
    ["Paulo Henrique", 39, "Ciência da Computação", [8.6, 8.9, 9.0]],
    ["Bruno", 27, "Engenharia de Software", [7.2, 7.5, 6.9]],
    ["Beatriz Alves", 21, "Engenharia de Software", [9.1, 9.4, 8.8]],
    ["Camila", 20, "Sistemas de Informação", [8.4, 8.0, 8.9]],
    ["Roberto Carlos", 33, "Engenharia de Software", [6.5, 7.0, 7.2]],
    ["Vanessa", 22, "Análise e Desenvolvimento de Sistemas", [9.0, 9.3, 8.9]],
    ["Thiago Martins", 29, "Ciência da Computação", [8.0, 7.8, 8.2]],
    ["Aline Souza", 26, "Sistemas de Informação", [7.5, 8.1, 7.9]],
    ["Diego", 24, "Análise e Desenvolvimento de Sistemas", [8.7, 8.5, 9.1]]
]

while True:
    print("1- Exibir Alunos da Turma de TI\n"
          "2- Pesquisar Dados da Turma de TI por Filtro\n"
          "3- Buscar Aluno da Turma de TI\n"
          "4- Calcular/Exibir Media dos Alunos da Turma de TI\n"
          "5- Cadastrar um Novo Aluno na Turma de TI\n"
          "6- Gerar Codigo dos Alunos da Turma de TI\n"
          "7- Gerar Relatorio de Aprovação da Turma\n"
          "8- Remover um Aluno da Turma de TI\n"
          "9- Mostrar Lista de Alunos Removidos\n"
          "0- Sair")
    opcao = int(input("\nDigite uma opção: "))

    if opcao == 1:
        print("\n1- Exibir Alunos da Turma de TI")
        print("-"*99)

    elif opcao == 2:
        print("\n2- Pesquisar Dados da Turma de TI por Filtro")
        print("-"*99)

    elif opcao == 3:
        print("\n3- Buscar Aluno da Turma de TI")
        print("-"*99)

    elif opcao == 4:
        print("\n4- Calcular/Exibir Media dos Alunos da Turma de TI")
        print("-"*99)

    elif opcao == 5:
        print("\n5- Cadastrar um Novo Aluno na Turma de TI")
        print("-"*99)

    elif opcao == 6:
        print("\n6- Gerar Codigo dos Alunos da Turma de TI")
        print("-"*99)

    elif opcao == 7:
        print("\n7- Gerar Relatorio de Aprovação da Turma")
        print("-"*99)

    elif opcao == 8:
        print("\n8- Remover um Aluno da Turma de TI")
        print("-"*99)

    elif opcao == 9:
        print("\n9- Mostrar Lista de Alunos Removidos")
        print("-"*99)

    elif opcao == 0:
        print("\n0- Sair")
        print("-"*99)
        break

    else:
        print("\nOpção Invalida!\nTente Novamente.\n")

print("\nEncerrando Programa...\n")
print("="*99)