import funcoes as f

def categoria_maior_consumo(): 
    f.read_key()
    pass
def mes_maior_gasto(): 
    f.read_key()
    pass
def mes_menor_gasto():
    f.read_key()
    pass
def taxa_media_economia():
    f.read_key()
    pass
def tendencia_saldo():
    f.read_key()
    pass


def menu_analises():
    while True:
        f.limpar_tela()
        f.double_line()
        print('ANÁLISES DO USUÁRIO'.center(f.size,' '))
        f.double_line()
        print('1 - CATEGORIA QUE MAIS CONSOME ')
        print('2 - MÊS COM MAIOR GASTO')
        print('3 - MÊS COM MENOR GASTO')
        print('4 - TAXA MÉDIA DE ECONOMIA')
        print('5 - TENDÊNCIA DO SALDO')
        print('0 - VOLTAR')
        f.double_line()
        opcao = f.ler_opcao_menu(5)
        f.double_line()
        if opcao == 1:
            f.limpar_tela()
            categoria_maior_consumo()

        elif opcao == 2:
            f.limpar_tela()
            mes_maior_gasto()

        elif opcao == 3:
            f.limpar_tela()
            mes_menor_gasto()

        elif opcao == 4:
            f.limpar_tela()
            taxa_media_economia()

        elif opcao == 5:
            f.limpar_tela()
            tendencia_saldo()

        elif opcao == 0:
            f.limpar_tela()
            break

            
if __name__ == '__main__':
    menu_analises()


