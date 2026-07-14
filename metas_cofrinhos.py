import funcoes as f

'''
COFRINHO (SEM META)
->ID, NOME, DATA CRIACAO, VALOR ATUAL

COFRINHO (COM META)
->ID, NOME, OBJETIVO, DATA CRIACAO, VALOR ATUAL, VALOR FINAL DESEJADO,...
...PORCENTAGEM PARA COMPLETAR.

Relação com saldo:
    -> adicionar um valor ao cofrinho implica em descontar do saldo.
    -> deverá ser registrado um log.
    -> ao apagar um cofrinho, todo o valor dentro dele deve retornar ao saldo.
    -> editar valor inserido: 
    --quando o novo valor editado for menor que o antigo: COFRINHO -= vl_velho_inserido - nv_vl_inserido
                                                          SALDO += vl_velho_inserido - nv_vl_inserido
                                                        
    --quando o novo valor editado for maior que o antigo: COFRINHO += vl_novo - vl_antigo
                                                             SALDO -= vl_novo - vl_antigo

-> cofrinhos podem ser criados livremente.
-> cofrinhos podem ser criados sem ter nenhuma quantidade dentro deles.
-> excluir um cofrinho faz com que o valor presente nele seja...
depositado no saldo.
-> deverá ter opção de corrigir o valor, isso não terá efeito no saldo...
logo poderá ser feito livremente

METAS
-> metas adicionarão atributos como VALOR FINAL DESEJADO e...
PORCENTAGEM PARA COMPLETAR ao cofrinho.
-> para uma meta existir é necessário que existam cofrinhos criados e...
sem metas à eles atribuídos.
->
'''

def criar_cofrinho():
    pass


def editar_cofrinho():
    pass


def excluir_cofrinho():
    pass


def depositar_vl_cofrinho():
    pass


def retirar_vl_cofrinho():
    pass


def listar_cofrinhos():
    pass


def consultar_dados_do_cofrinho():
    pass


def criar_meta():    
    f.read_key()
    pass


def editar_meta():
    f.read_key()
    pass


def excluir_meta():
    f.read_key()
    pass


def listar_metas_e_porcentagem():
    f.read_key()
    pass


def menu_metas():
    while True:
        f.limpar_tela()
        f.double_line()
        print('METAS & COFRINHOS'.center(f.size,' '))
        f.double_line()
        print(
        '1 - CRIAR COFRINHO\n'
        '2 - EDITAR COFRINHO\n'
        '3 - EXCLUIR COFRINHO\n'
        '4 - DEPOSITAR QUANTIA NO COFRINHO\n'
        '5 - RETIRAR QUANTIA DO COFRINHO\n'
        '6 - LISTAR COFRINHOS\n'# nome cofrinho | valor | Meta (sim/não)
        '7 - CONSULTAR DADOS DO COFRINHO\n'
        '8 - CRIAR META\n'
        '9 - EDITAR META\n'# mudar valor desejado
        '10 - EXCLUIR META\n'
        '11 - LISTAR METAS E PORCENTAGEM\n'
        '0 - VOLTAR'
        )
        f.double_line()
        opcao = f.ler_opcao_menu(10)
        f.double_line()
        
        if opcao == 1:
            f.limpar_tela()
            criar_cofrinho()

        elif opcao == 2:
            f.limpar_tela()
            editar_cofrinho()

        elif opcao == 3:
            f.limpar_tela()
            excluir_cofrinho()

        elif opcao == 4:
            f.limpar_tela()
            depositar_vl_cofrinho()

        elif opcao == 5:
            f.limpar_tela()
            retirar_vl_cofrinho()

        elif opcao == 6:
            f.limpar_tela()
            listar_cofrinhos()

        if opcao == 7:
            f.limpar_tela()
            consultar_dados_do_cofrinho()
            criar_meta()

        elif opcao == 8:
            f.limpar_tela()
            criar_meta()

        elif opcao == 9:
            f.limpar_tela()
            editar_meta()

        elif opcao == 10:
            f.limpar_tela()
            excluir_meta()
            
        elif opcao == 11:
            f.limpar_tela()
            listar_metas_e_porcentagem()

        elif opcao == 0:
            f.limpar_tela()
            break

if __name__ == '__main__':
    menu_metas()

