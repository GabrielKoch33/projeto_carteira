import funcoes as f

def adicionar_despesa():
    f.read_key()
    pass
def editar_despesa():
    f.read_key()
    pass
def remover_despesa():
    f.read_key()
    pass
def listar_despesa():
    # print('='* u.size)
    # print('LISTA DE DESPESAS'.center(u.size,' '))
    # print('='* u.size)
    # valor, descricao, categoria, data
    f.read_key()
    pass
def buscar_por_descricao():
    f.read_key()
    pass
def buscar_por_categoria():
    f.read_key()
    pass
def buscar_por_periodo():
    f.read_key()
    pass


def menu_despesa():
    while True:
        f.limpar_tela()
        f.double_line()
        print('DESPESAS'.center(f.size,' '))
        f.double_line()
        print('1 - ADICIONAR DESPESA')
        print('2 - EDITAR DESPESA')
        print('3 - REMOVER DESPESA')
        print('4 - LISTAR DESPESAS')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        f.double_line()
        opcao = f.ler_opcao_menu(7)
        f.double_line()
        
        if opcao == 1:
            f.limpar_tela()
            adicionar_despesa()

        elif opcao == 2:
            f.limpar_tela()
            editar_despesa()

        elif opcao == 3:
            f.limpar_tela()
            remover_despesa()

        elif opcao == 4:
            f.limpar_tela()
            listar_despesa()

        elif opcao == 5:
            f.limpar_tela()
            buscar_por_descricao()

        elif opcao == 6:
            f.limpar_tela()
            buscar_por_categoria()

        elif opcao == 7:
            f.limpar_tela()
            buscar_por_periodo()

        elif opcao == 0:
            f.limpar_tela()
            break

if __name__ == '__main__':
    menu_despesa()
