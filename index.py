import time
import os
import msvcrt
from collections import deque

cursos ={
    "1": {
        "materia": "matematica",
        "cargahoraria": 40,
        "professor": "Mauricio",
    },
    "2": {
        "materia": "portugues",
        "cargahoraria": 55,
        "professor": "prof",  
    },
    "3": {
        "materia": "quimica",
        "cargahoraria": 40,
        "professor": "prof",
    },
    "4": {
        "materia": "historia",
        "cargahoraria": 45,
        "professor": "Luciana"
    },
    "5": {
        "materia": "geografia",
        "cargahoraria": 50,
        "professor": "Carlos"
    },
    "6": {
        "materia": "ingles",
        "cargahoraria": 35,
        "professor": "Amanda"
    },
    "7": {
        "materia": "fisica",
        "cargahoraria": 60,
        "professor": "Dr. Roberto"
    },
    "8": {
        "materia": "artes",
        "cargahoraria": 30,
        "professor": "Juliana"
    }
}

alunos = {
    "1": {
        "nome": "Adriano",
        "idade": 13,
        "serie": 6,
        "periodo": "Manhã",
        "matricula": deque([1, 3, 2])
    },
    "2": {
        "nome": "Bianca",
        "idade": 13,
        "serie": 7,
        "periodo": "Manhã",
        "matricula": deque([1, 3, 2])
    },
    "3": {
        "nome": "Conceição",
        "idade": 12,
        "serie": 6,
        "periodo": "Tarde",
        "matricula": deque([1, 3, 2])
    },
    "4": {
        "nome": "Diego",
        "idade": 14,
        "serie": 8,
        "periodo": "Tarde",
        "matricula": deque([4, 5])
    },
    "5": {
        "nome": "Eduarda",
        "idade": 13,
        "serie": 7,
        "periodo": "Manhã",
        "matricula": deque([2, 6])
    },
    "6": {
        "nome": "Felipe",
        "idade": 12,
        "serie": 6,
        "periodo": "Manhã",
        "matricula": deque([1, 7])
    },
    "7": {
        "nome": "Gabriela",
        "idade": 15,
        "serie": 9,
        "periodo": "Tarde",
        "matricula": deque([3, 8])
    },
    "8": {
        "nome": "Hugo",
        "idade": 14,
        "serie": 8,
        "periodo": "Manhã",
        "matricula": deque([2, 4, 6])
    }
    

}

# atribuir cursos a alunos
# citar cursos de um aluno
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def anima_pontos():
    for i in range(3):
        print("." * (i+1), end='\r') # imprime os pontos e sobrescreve na linha
        time.sleep(0.5) # espera 0.5 segundos

def menu(alunos:dict, cursos: dict ) -> None:
    while True:
        resposta = int(input("Selecione um item \n" \
            "[1] - Listar Alunos \n" \
            "[2] - Listar Cursos \n" \
            "[3] - Adicionar um Curso \n" \
            "[4] - Adicionar um Aluno \n" \
            "[5] - Edição de Curso \n"\
            "[0] - Encerrar o programa \n"))
        
        match(resposta):

            case 0:
                anima_pontos()
                time.sleep(0.5)
                print("Encerrando programa")
                time.sleep(1)
                break

            case 1:
                anima_pontos()
                print("Listagem de alunos")
                time.sleep(1.5)
                limpar_terminal()
                listagemAlunos(alunos)

            case 2:
                anima_pontos()
                print("Listagem Cursos")
                time.sleep(1.5)
                listagemCursos(cursos)
            
            case 3:
                anima_pontos
                print("Adicionar um curso")
                time.sleep(1.5)
                adicionarCurso(cursos)
                
            case 4:
                anima_pontos()
                print("Adicionar um Aluno")
                time.sleep(1.5)
                adicionarAluno(alunos)

            case 5:
                anima_pontos()
                print("Editar curso")
                time.sleep(1.5)
                edicaoCursos(alunos, cursos)
                

            case _:
                print("Numero invalido!")
                continue
           
#Lista todos os alunos \opção 1
def listagemAlunos(lista: dict) -> None:
    limpar_terminal()
    for dados in lista.values():
        print("-" * 30)
        print(f"O nome é: {dados["nome"]}")
        print(f"Tem {dados["idade"]} anos")
        print(f"Está na {dados["serie"]}ª série")
        print(f"Estuda de {dados["periodo"]}")

    print("-" * 30)
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

#Lista todos os cursos \opção 2
def listagemCursos(lista: dict) -> None:

    limpar_terminal()
    for dados in lista.values():
        print("-" * 30)
        print(f"A materia do curso é: {dados["materia"]}")
        print(f"Tem {dados["cargahoraria"]} horas de aula")
        print(f"Com o professor {dados["professor"]}")

    print("-" * 30)
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

#Adicionar um Curso \opção 3
def adicionarCurso(lista:dict ) -> None:

    id = str(len(lista) + 1)
    limpar_terminal()

    materia = str(input("Qual a materia do Curso: "))    
    cargahoraria = int(input("Qual a carga horaria: "))
    professor = str(input("Qual o professor: "))

    lista.update({
        id: {
            "materia": materia,
            "cargahoraria": cargahoraria,
            "professor": professor,
        }
    })
    print(f"Curso {materia} de codigo {id} adicionado com sucesso! \n")

    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

# Adiciona um aluno \opção 4
def adicionarAluno(lista:dict) -> None:
    id = str(len(lista) + 1)

    limpar_terminal()

    nome = str(input("Qual o nome do aluno: "))
    idade = int(input("Qual idade do aluno: "))
    serie = int(input("Qual serie dele: "))
    periodo = str(input("Qual periodo: "))

    lista.update({
        id:{
            "nome": nome,
            "idade": idade,
            "serie": serie,
            "periodo": periodo,
        }
    })
    print(f"Aluno {nome} de codigo {id} adicionado com sucesso! \n")
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

#Menu de cursos ->

#Menu Cursos
def edicaoCursos(alunos:dict, cursos:dict):
    

    while True: 

        limpar_terminal()

        resposta = int(input(
            "Selecione uma opção \n" \
            "[0] - Voltar menu \n" \
            "[1] - Matricular Curso \n" \
            "[2] - Excluir curso \n" \
            "[3] - Listar uma sala do curso \n"))
        
        match (resposta):
            case 0 :
                print("Voltar menu inicial")
                limpar_terminal()
                time.sleep(1)
                break

            case 1:
                anima_pontos()
                print("Matricular Curso")
                time.sleep(1.5)
                limpar_terminal()
                matricularCurso(alunos, cursos)

            case 2:
                anima_pontos()
                print("Excluir curso")
                time.sleep(1.5)
                limpar_terminal()
                removerCurso(alunos, cursos)

            case 3:
                anima_pontos()
                print("Motrar sala do curso")
                time.sleep(1.5)
                limpar_terminal()
                listaClasse(alunos, cursos)


            case _:
                print("Escolha invalída")
                pass

#Mastricular cursos \ Opção 1
def matricularCurso(alunos: dict, cursos:dict):
    
    #Listar alunos
    while True:
        resposta = input("Listar Alunos? [S/N]: ").upper()
        if resposta == 'N':
            break
        elif resposta == 'S':
            listagemAlunos(alunos)
            break
        else:
            print("Resposta invalida!")
            time.sleep(1.5)

    #Escolha Aluno
    while True:
        idAluno = input("Qual aluno quer editar: ").strip()
        if idAluno not in alunos:
            print("Número inválido.")
            time.sleep(1.5)
        else:
            escolhido = alunos[idAluno]
            print(f"Aluno escolhido: {escolhido['nome']}")
            time.sleep(1.5)
            break

    #Adiciona Curso
    while True:
        idCurso = input("Qual curso quer adicionar (ou 'sair' para terminar)? ").strip()
        if idCurso.lower() == 'sair':
            break
        elif idCurso not in cursos:
            print("Número inválido.")
            time.sleep(1.5)
        else:
            escolhido.setdefault('matricula', deque())
            # Garante que a chave 'matricula' está presente
            if idCurso not in escolhido["matricula"]:
                escolhido["matricula"].append(idCurso)
                print(f"Curso '{idCurso}' adicionado.")
                time.sleep(0.5)
            else:
                print("Aluno já está matriculado nesse curso.")
                time.sleep(1.5)
                break
        
#Excluir Curso \ Opção 2
def removerCurso (alunos:dict, cursos:dict):
    idCurso = int(input("Digite o código do curso: "))
    
    if str(idCurso) not in cursos:
        print(f"Curso com ID {idCurso} não encontrado.")
        time.sleep(1.5)
        return

    valor_removido = cursos.pop(str(idCurso))

    limpar_terminal()
    anima_pontos()

    print(f"Curso {idCurso} de matéria {valor_removido["materia"]} foi deletado")

    for alunoId, aluno in alunos.items():

        if "matricula" in aluno and idCurso in aluno["matricula"]:
            aluno['matricula'].remove(idCurso)
            print(f"Aluno {aluno['nome']} desmatriculado do curso {idCurso}")

    time.sleep(1)
    print("-" * 30)
    print(f"Curso {idCurso} desmatriculado com sucesso")
    print("-" * 30)
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

#Listar a sala de um curso \3
def listaClasse(alunos: dict, cursos:dict):
    idCurso = str(input("digite o código do curso que quer ver: "))

    if idCurso not in cursos:
        print(f"Curso com ID {idCurso} não encontrado.")
        time.sleep(1.5)
        return


    print(f"Curso escolhido {cursos[idCurso]['materia']}")
    time.sleep(1.5)

    for aluno in alunos.values():
        if "matricula" in aluno and int(idCurso) in aluno["matricula"]:
            print(f"{aluno['nome']} está matriculado nesse curso") 
        
    print("-" * 30)
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

if __name__ == "__main__":
    menu(alunos, cursos)
