import funcoes as f
import estruturas_dados as est

def criar_cofrinho():

    pass

def editar_cofrinho():
    pass

def excluir_cofrinho():
    pass

def redefinir_val():
    pass

def listar_cofrinhos():
    pass

def menu_cofrinhos():
    while True:
        f.limpar_tela()
        f.double_line()
        print('COFRINHOS'.center(f.size,' '))
        f.double_line()
        print(
            f' 1 - CRIAR COFRINHO\n'
            f' 2 - EDITAR COFRINHO\n'
            f' 3 - EXCLUIR COFRINHO\n'
            f' 4 - REDEFINIR VALOR TOTAL\n'
            f' 5 - LISTAR COFRINHOS\n'
            f' 0 - VOLTAR'
        )

        f.double_line()
        opcao = f.ler_opcao_menu(5)
        f.double_line()
        
        if opcao == 1:
            f.limpar_tela()
            criar_cofrinho()
            f.double_line()
            f.read_key()            

        elif opcao == 2:
            f.limpar_tela()
            editar_cofrinho()
            f.double_line()
            f.read_key()

        elif opcao == 3:
            f.limpar_tela()
            excluir_cofrinho()
            f.double_line()
            f.read_key()

        elif opcao == 4:
            f.limpar_tela()
            redefinir_val()
            f.double_line()
            f.read_key()

        elif opcao == 5:
            f.limpar_tela()
            listar_cofrinhos()
            f.double_line()
            f.read_key()

        elif opcao == 0:
            f.limpar_tela()
            break

if __name__ == '__main__':
    menu_cofrinhos()