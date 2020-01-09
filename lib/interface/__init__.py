def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mErro: Please digite um number válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário\033[31m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-'*tam

def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for bagui in lista:
        print(f'\033[33m{c}\033[m - \033[34m{bagui}\033[m')
        c+=1
    print(linha())
    opc=leiaint('\033[32mSua opção: \033[m')
    return opc

