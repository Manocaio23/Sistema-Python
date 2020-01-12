from lib.interface import *
from lib.arquivo import*
from time import sleep

arq='Manocaio.txt'

if not arquivoExiste(arq):
     criarArquivo(arq)

while True:
    resposta=menu(['Ver Pessoas cadastradas','Cadastrar nova pessoa','sair'])

    if resposta==1:
        #Opção para lsitar o conteúdo
        lerArquivo(arq)

    elif resposta==2:
        #opção de cadastrar uma pessoa
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome:'))
        idade=int(input('Idade:'))
        cadastrar(arq, nome,idade)

    elif resposta==3:
         print('Saindo...')
         break

    else:
       cabecalho('\033[31mPlease digita um valor valido\033[m')
    sleep(2)

