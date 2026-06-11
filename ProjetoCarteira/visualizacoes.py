import utils as u
import main as m

def pizzaCategoria():
    u.readKey()
    pass
def barrasCategoria(): 
    u.readKey()
    pass
def evolSaldo(): 
    u.readKey()
    pass
def linhaDespesas():
    u.readKey()
    pass


def menuVisualizacoes(): 
        u.limparTela()
        print('===============================')
        print('--- VISUALIZAÇÕES & GRÁFICOS ---')
        print('===============================')
        print('1 - PIZZA POR CATEGORIA')
        print('2 - BARRAS POR CATEGORIA')
        print('3 - EVOLUÇÃO SALDO')
        print('4 - LINHA DE DESPESAS')
        print('5 - VOLTAR')
        print('===============================')
        opcao = input('Digite a opção desejada: ')
        print('===============================')
        if opcao == '1':
            u.limparTela()
            pizzaCategoria()
        elif opcao == '2':
            u.limparTela()
            barrasCategoria()
        elif opcao == '3':
            u.limparTela()
            evolSaldo()
        elif opcao == '4':
            u.limparTela()
            linhaDespesas()
        elif opcao == '5':
            m.mainMenu()
        else:
            u.limparTela()
            print('Opcão Inválida')
            u.readKey()
            menuVisualizacoes()

if __name__ == '__main__':
    menuVisualizacoes()
