import funcoes as f

def criar_meta():
    '''
    INT ID
    INT ID COFRINHO
    STR OBJETIVO
    FLOAT VALOR DESEJADO
    (% será calculada no momento exibição)
    '''
    pass

def editar_meta():
    pass

def excluir_meta():
    pass

def listar_metas():
    pass

def menu_metas():
    while True:
        f.limpar_tela()
        f.double_line()
        print('METAS'.center(f.size,' '))
        f.double_line()
        print(
            f' 1 - ATRIBUIR META\n'
            f' 2 - EDITAR META\n'
            f' 3 - EXCLUIR META\n'
            f' 4 - LISTAR METAS\n'
            f' 0 - VOLTAR'
        )

        f.double_line()
        opcao = f.ler_opcao_menu(4)
        f.double_line()
        
        if opcao == 1:
            f.limpar_tela()
            criar_meta()
            f.double_line()
            f.read_key()            

        elif opcao == 2:
            f.limpar_tela()
            editar_meta()
            f.double_line()
            f.read_key()


        elif opcao == 3:
            f.limpar_tela()
            excluir_meta()
            f.double_line()
            f.read_key()


        elif opcao == 4:
            f.limpar_tela()
            listar_metas()
            f.double_line()
            f.read_key()

        elif opcao == 0:
            f.limpar_tela()
            break

if __name__ == '__main__':
    menu_metas()