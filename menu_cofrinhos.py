import funcoes as f
import estruturas_dados as est

def criar_cofrinho():
    while True:
        nome_cofrinho = input('Dê um nome para o cofrinho: ').strip().lower()

        if not nome_cofrinho:
            return 'Nomes vazios não são válidos! Voltando para o menu...'
        else:
            break
    
    while True:
        data_cofrinho = f.converte_data()

        if not data_cofrinho:
            f.double_line()
            print("Erro: Digite exatamente 8 números.")
            f.double_line()
            continue # se voltar erro, pede data novamente
        else:
            break

    while True:
        valor_cofrinho = input('Digite o valor em R$ da entrada: ')
        valor_cofrinho = f.converte_moeda(valor_cofrinho)

        if isinstance(valor_cofrinho,str):
            print(valor_cofrinho)
            continue
        else:
            break

    id_cofrinho = f.gera_id(est.lista_cofrinhos)
    est.lista_cofrinhos.append({
                            "id": id_cofrinho,
                            "nome": nome_cofrinho,
                            "data_criacao": data_cofrinho, # NÃO PODERÁ SER EDITADA
                            "valor atual": valor_cofrinho, # 
                            "auto_deposito": False,        # INICIALMENTE ESTARÁ DESABILITADO 
                            "qtd_automatica": 0,           # SERÁ PEDIDA QUANDO ATIVAR O AUTO DEPOSITO
                            "meta": False,                 # SERÁ CRIADA DE FORMA ALHEIA 
                            })

    return 'Cofrinho cadastrado com sucesso'

def editar_cofrinho():
    pass

def excluir_cofrinho():
    pass

def redefinir_val():
    pass

def menu_cofrinhos():
    while True:
        f.limpar_tela()
        f.double_line()
        print('COFRINHOS'.center(f.size,' '))
        f.double_line()
        print(
            f' 1 - CRIAR COFRINHO'
            f' 2 - EDITAR COFRINHO'
            f' 3 - EXCLUIR COFRINHO'
            f' 4 - REDEFINIR VALOR TOTAL'
            f' 0 - VOLTAR'
        )

        f.double_line()
        opcao = f.ler_opcao_menu(4)
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

if __name__ == '__main__':
    menu_cofrinhos()