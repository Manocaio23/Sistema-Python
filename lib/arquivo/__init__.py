from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a= open(nome,'rt')# abrir o arquivo em modo texto
        a.close()
    except FileNotFoundError:# se o arquivo não for encontrado
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome, 'wt+')#escrever um arquivo de texto
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a= open(nome,'rt')
    except:
        print('Erro ao ler o aquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado=linha.split(';')
            dado[1]= dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido',idade=0):
    try:
        a=open(arq,'at')#a de appende que insere
    except:
        print('Houve um erro na abertura')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um Erro na hora de escrever os dados')
        else:
            print(f'Novo resgistro e {nome} foi adicionado')
            a.close()