import funcoes as f
'''
Cofrinhos:
    -> um cofrinho poderá ter ou não ter uma meta. (0:1).
    -> cofrinhos terão atributos como: Nome, Objetivo, Qtd Atual, Qtd Desejada, Valor Faltante.
    -> por limitações que me impedem de sincronizar os rendimentos do cofrinho, a função de editar
    .. será algo recorrente (sempre alterar ao usar o sistema)


Metas:
    -> poderão ser criadas para cofrinhos ou para conquistas (ex: alcançar 6k de saldo).
    -> Metas se referem a atributos financeiros, não coisas materiais (comprar um carro ou item X)

Relação com saldo:
    -> adicionar um valor ao cofrinho implica em descontar do saldo.
    -> deverá ser registrado um log.
    -> ao apagar um cofrinho, todo o valor dentro dele deve retornar ao saldo.
    -> editar valor inserido: 
-> cofr -= vl_velho_inserido - nv_vl_inserido) & (saldo += vl_velho_inserido - nv_vl_inserido) (quando nv_vl < vl_antigo)
-> cofr += (vl_novo - vl_antigo) & (saldo -= vl_novo - vl_antigo) (quando nv_vl > vl antigo)
'''

def criar_cofrinho():
    pass


def editar_cofrinho():
    pass


def excluir_cofrinho():
    pass


def inseir_vl_cofrinho():
    pass


def retirar_vl_cofrinho():
    pass


def editar_vl_inserido_cofrinho():
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
        print('METAS & COFRINHOS'.center(f.size,' '))
        f.double_line()
        print(
        '1 - CRIAR COFRINHO\n'
        '2 - EDITAR COFRINHO\n'
        '3 - EXCLUIR COFRINHO\n'
        '4 - INSERIR QUANTIA NO COFRINHO\n'
        '5 - RETIRAR QUANTIA DO COFRINHO\n'
        '6 - EDITAR QUANTIA INSERIDA\n'
        '7 - CRIAR META\n'
        '8 - EDITAR META\n'
        '9 - EXCLUIR META\n'
        '10 - LISTAR METAS E PORCENTAGEM\n'
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
            inseir_vl_cofrinho()

        elif opcao == 5:
            f.limpar_tela()
            retirar_vl_cofrinho()

        elif opcao == 6:
            f.limpar_tela()
            editar_vl_inserido_cofrinho()

        if opcao == 7:
            f.limpar_tela()
            criar_meta()

        elif opcao == 8:
            f.limpar_tela()
            editar_meta()

        elif opcao == 9:
            f.limpar_tela()
            excluir_meta()

        elif opcao == 10:
            f.limpar_tela()
            listar_metas_and_porcentagem()

        elif opcao == 0:
            f.limpar_tela()
            break

if __name__ == '__main__':
    menu_metas()

