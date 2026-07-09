import funcoes as f

def criar_meta():

    
    f.read_key()
    pass
def editar_meta():
    f.read_key()
    pass
def excluir_meta():
    f.read_key()
    pass
def listar_metas_and_porcentagem():
    f.read_key()
    pass

#Campos: nome, valor alvo, prazo
#Indicadores: percentual concluído e valor restante
#Dar uma sugestão de X por Mês para atingir a Meta
def menu_metas():
    while True:
        f.limpar_tela()
        f.double_line()
        print('METAS'.center(f.size,' '))
        f.double_line()
        print('1 - CRIAR META')
        print('2 - EDITAR META')
        print('3 - EXCLUIR META')
        print('4 - LISTAR METAS E PORCENTAGEM')
        print('0 - VOLTAR')
        f.double_line()
        opcao = f.ler_opcao_menu(4)
        f.double_line()
        
        if opcao == 1:
            f.limpar_tela()
            criar_meta()

        elif opcao == 2:
            f.limpar_tela()
            editar_meta()

        elif opcao == 3:
            f.limpar_tela()
            excluir_meta()

        elif opcao == 4:
            f.limpar_tela()
            listar_metas_and_porcentagem()

        elif opcao == 0:
            f.limpar_tela()
            break

if __name__ == '__main__':
    menu_metas()

