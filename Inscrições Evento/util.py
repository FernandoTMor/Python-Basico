import datetime

def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0])
        leitor.close()
    except:
        pass

def inscricao(lista):
    matricula = input('Informe matrícula: ')
    if matricula in lista:
        print('Esta matrícula já foi inscrita no evento')
    else:
        lista.append(matricula)
        nome = input('Nome: ')
        nome = nome.upper()
        email = input('Email: ')
        email = email.lower()
        escritor = open('inscricoes.dat','a')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')
        escritor.close()

def listagem():
    try:
        leitor = open('inscricoes.dat','r',encoding='utf8')
        for linha in leitor:
            vetor_linha = linha.split(';')
            print('Nome:',vetor_linha[1],'Matrícula:',vetor_linha[0])

        leitor.close()
    except:
        print('Sem inscrições até o momento')

def entrada(lista):
    matricula = input('Digite a matricula para entrar no evento')
    if matricula in lista:
        escritor = open('entrada.dat', 'a')
        escritor.write(matricula +'-----'+ datetime.time)
    else:
        print('Nao foi possivel encontrar matricula para entrar no evento')


def saida(lista):
    matricula = input('Digite a matricula para sair do evento')
    if matricula in lista:
        escritor = open('saida.dat', 'a')
        escritor.write(matricula +'-----'+ datetime.time)
    else:
        print('Nao foi possivel encontrar matricula para sair do evento')