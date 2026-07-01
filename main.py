import time
import entradas as ent
import despesas as des
import categorias as cat
import relatorios as rel
import estatisticas as est
import projeto_carteira.graficos as views
import analises as anl
import metas as met
import funcoes as f
import dados

def main_menu():
    while True:
        f.limpar_tela()
        f.double_line()
        print('CARTEIRA DE GABRIEL'.center(f.size,' '))
        f.double_line()
        print('1 - ENTRADAS')
        print('2 - DESPESAS')
        print('3 - CATEGORIAS')
        print('4 - RELATÓRIOS')
        print('5 - ESTATÍSTICAS')
        print('6 - VISUALIZAÇÕES')#graficos
        print('7 - ANÁLISES AUTOMÁTICAS')
        print('8 - METAS FINANCEIRAS')
        print('0 - SALVAR E SAIR')
        f.double_line()
        opcao = f.ler_opcao_menu(8)
        f.double_line()
        if opcao == 1:
            ent.menu_entradas()
        elif opcao == 2:
            des.menu_despesa()
        elif opcao == 3:
            cat.menu_categorias()
        elif opcao == 4:
            rel.menu_relatorio()
        elif opcao == 5:
            est.menu_estatisticas()
        elif opcao == 6:
            views.menu_visualizacoes()
        elif opcao == 7:
            anl.menu_analises()
        elif opcao == 8:
            met.menu_metas()
        elif opcao == 0:
            print('Salvando...')
            f.pause()
            break

if __name__ == '__main__':
    '''
    Fazer verificação: se o arquivo que guarda os dados estiver vazio
    Então pedimos o saldo pela 1ª e única vez
    Senão, Abrimos o arquivos e pegamos o saldo armazenado.
    '''
    while True:
        f.saldo = input('Qual é o seu saldo atual?: ').strip()

        if not f.saldo:
            print('Valores vazios não são permitidos!')
            continue

        try:
            f.saldo = f.saldo.replace('.', '')
            f.saldo = f.saldo.replace(',', '.')
            f.saldo = float(f.saldo)

        except:
            print('Por favor, insira um valor numérico válido.')
            continue

        if f.saldo < 0:
            print('Valores negativos não são permitidos!')
            continue

        break

    print('Iniciando...')
    time.sleep(1)
    print('Carregando Arquivos e Dados...')
    time.sleep(1)
    print('Pronto')
    main_menu()
