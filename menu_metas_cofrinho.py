import funcoes as f
import estruturas_dados as est
import menu_cofrinhos as mCofr
import menu_metas as mMetas
import menu_mov_meta_cofr as mMov
#from rich import print
#print("[red]Texto vermelho usando Rich[/red]")
#print("[bold blue]Texto azul em negrito usando Rich[/bold blue]")

'''
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
-> para uma meta existir é necessário que existam cofrinhos criados e...
sem metas à eles atribuídos.


Metas e Depósitos Automaticos podem ser criadas durante a criação de cofrinhos
assim como podem ser inseridos posteriormentes de forma separada


'''

def listar_cofrinhos():
    if not est.lista_cofrinhos:
        return 'Registro de cofrinhos vazio. Nenhum cofrinho para listar'
    
    else:
        f.imprime_colunas('COFRINHOS')
        print(
            f'{"ID":<5}'
            f'{"NOME":<20}'
            f'{"DATA CRIAÇÃO":<15}'
            f'{"VALOR ATUAL":<16}'
            f'{"DEPÓSITO AUTOMÁTICO":<22}'   
            f'{"QUANTIA AUTOMATICA":22}'
            f'{"META":15}'
            )
        f.line()

        num_registros = 0
        for item in est.lista_cofrinhos:
            data_ = item['data_criacao'].strftime("%d/%m/%Y")
            num_registros += 1
            pass

        f.read_key()
        pass

def listar_metas():
    f.read_key()
    pass

def menu_cofrinhos_e_metas():
    f.line()
    print(
        f'\033[31m!!! AVISO !!!\033[0m\n' # Deixando o texto em vermelho
        f'Metas e Depósito Automático (DA) são propriedades dos Cofrinhos.\nLogo, para realizar quaisquer atividades com Metas e DA '
        f'deve-se acessar a opção 2 e selecionar "Editar Meta" ou "Editar Depósito Automático".'
        )
    f.line()
    f.read_key()

    while True:
        f.limpar_tela()
        f.double_line()
        print('METAS & COFRINHOS'.center(f.size,' '))
        f.double_line()
        print(
            f' 1 - GERENCIAR COFRINHOS\n'
            # Criar, editar, excluir
            f' 2 - GERENCIAR METAS\n'
            # editar meta existente, atribuir meta, remover meta
            f' 3 - GERENCIAR MOVIMENTAÇÃO\n'
            # retirar, depositar, editar mov, 
            f' 4 - RELATÓRIO\n'
            # Lista todos os cofres, com ou sem meta
            # Id, nome, dtcriacao, val atual, auto dep(float/false), meta(float/false) 
            # objetivo, valor desejado, %
            f' 0 - VOLTAR'
        )
        
        f.double_line()
        opcao = f.ler_opcao_menu(4)
        f.double_line()
        
        if opcao == 1:
            f.limpar_tela()
            mCofr.menu_cofrinhos()
            f.double_line()
            f.read_key()            

        elif opcao == 2:
            f.limpar_tela()
            mMetas.menu_metas()
            f.double_line()
            f.read_key()


        elif opcao == 3:
            f.limpar_tela()
            mMov.menu_movimentacoes_cofr_metas()
            f.double_line()
            f.read_key()


        elif opcao == 4:
            f.limpar_tela()
            msg = listar_cofrinhos()
            print(msg)
            f.double_line()
            f.read_key()


        elif opcao == 5:
            f.limpar_tela()
            msg = listar_metas()
            print(msg)
            f.double_line()
            f.read_key()

        elif opcao == 0:
            f.limpar_tela()
            break


if __name__ == '__main__':
    menu_cofrinhos_e_metas()

