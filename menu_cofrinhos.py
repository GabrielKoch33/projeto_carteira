import funcoes as f
import estruturas_dados as est

def criar_cofrinho():
    '''
    INT id,
    STR NOME,
    DATETIME data criacao,
    FLOAT valor inicial
    (definir/redefinir o valor inicial n afeta o saldo),
    BOOL auto deposito,
    FLOAT valor auto deposito
    FLOAT id meta 
    (acessar campo: ['valor meta'] para buscar o valor desejado)
    '''
    while True:
        nome_cofr = input('Digite um nome para o cofrinho: ').strip().lower()
        if not nome_cofr:
            f.double_line()
            print('ERRO: Tente novamente!')
            f.double_line()
        else:
            break

    while True:
        dt_criacao_cofr = f.converte_data()
        if not dt_criacao_cofr:
            f.double_line()
            print('ERRO: Digite exatamente 8 números.')
            f.double_line()
        else:
            break

    while True:
        valor_cofr = input('Digite o valor de seu cofrinho em R$: ').strip()
        if valor_cofr == '0':
            valor_cofr = 0
        else:
            valor_cofr = f.converte_moeda(valor_cofr)
            if isinstance(valor_cofr,str):
                f.double_line()
                print(f'{valor_cofr}\nTente novamente!')
                f.double_line()
                continue
        break

    opt_auto_depo = input(f'Deseja ativar o Auto-Depósito para esse Cofrinho? [Y/n]\nR: ').strip().upper()
    if opt_auto_depo == 'Y':
        bool_auto_dep = True

        while True:
            valor_auto_depo = input('Digite o valor (em R$) para ser depositado automaticamente: ').strip()
            valor_cofr = f.converte_moeda(valor_auto_depo)
            if isinstance(valor_auto_depo,str):
                f.double_line()
                print(f'{valor_auto_depo}\nTente novamente!')
                f.double_line()
                continue
            break

    else:
        bool_auto_dep = False
        valor_auto_depo = 0
        print('Caso deseje ativar o Auto-Depósito posteriormente, vá para a opção de "Editar Cofrinho"')
        f.pause()

    id_cofr = f.gera_id(est.lista_cofrinhos)
    est.lista_cofrinhos.append({
        "id_cofr":id_cofr,
        "nome_cofr":nome_cofr,
        "dt_cofr":dt_criacao_cofr,
        "val_atual_cofr":valor_cofr,
        "auto_depo":bool_auto_dep,
        "val_auto_depo":valor_auto_depo,
        "id_meta":None,
        })


def editar_cofrinho():


    pass

def excluir_cofrinho():
    pass

def redefinir_val():
    pass

def listar_cofrinhos():
    if not est.lista_cofrinhos:
        return 'Registro de entradas vazio. Nenhum cofrinho para listar!'
    else:
        f.imprime_colunas('COFRINHOS')
        print(
            f'{"ID":<5}',
            f'{"NOME":<30}',
            f'{"DATA":<12}',
            f'{"VALOR":<15}',
            f'{"AUTO DEPOSITO":<5}',
            f'{"VALOR AUTO DEPOSITO":<15}',
            f'{"META":<15}'
            )
        f.line()

        num_registros = 0
        for item in est.lista_cofrinhos:
            data_ = item['dt_cofr'].strftime("%d/%m/%Y")
            num_registros += 1
            campo_autodep_str = "Ativado" if item['auto_depo'] == True else "Desativado"
            campo_meta_str = 'finalizar, precisa procurar nos logs de meta onde o cofrinho atual esteja e retornar o valor de meta'
            print(
                f'{item["id_cofr"]:<5}'
                f'{item["nome_cofr"]:<30}'
                f'{data_:<12}'
                f'{item["val_atual_cofr"]:<15}'
                f'{campo_autodep_str:<5}'
                f'{item["val_auto_depo"]:<15}'
                f'{item["id_meta"]:<15}'
                )
        f.double_line()
        print(f'Total de registros: {num_registros}') 
        return 'Lista retornada com sucesso!'
    

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