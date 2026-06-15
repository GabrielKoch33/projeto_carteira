import utils as u
import main as m

def saldoAtual():
    u.readKey()
    pass
def totalEntradas():
    u.readKey()
    pass
def totalDespesdas():
    u.readKey()
    pass
def gastosPorCategoria(): 
    u.readKey()
    pass
def entradasPorCategoria():
    u.readKey()
    pass
def relatorioMensal():
    u.readKey()
    pass
def relatorioAnual():
    u.readKey()
    pass


def menuRelatorio():
    while True:
        u.limparTela()
        print('===============================')
        print('--- RELATÓRIOS ---')
        print('===============================')
        print('1 - SALDO ATUAL')
        print('2 - TOTAL DE ENTRADAS')
        print('3 - TOTAL DE DESPESAS')
        print('4 - GASTOS POR CATEGORIA')
        print('5 - ENTRADAS POR CATEGORIA')
        print('6 - RELATÓRIO MENSAL')
        print('7 - RELATÓRIO ANUAL')
        print('8 - VOLTAR')
        print('===============================')
        opcao = input('Digite a opção desejada: ')
        print('===============================')
        
        if opcao == '1':
            u.limparTela()
            saldoAtual()

        elif opcao == '2':
            u.limparTela()
            totalEntradas()

        elif opcao == '3':
            u.limparTela()
            totalDespesdas()

        elif opcao == '4':
            u.limparTela()
            gastosPorCategoria()

        elif opcao == '5':
            u.limparTela()
            entradasPorCategoria()

        elif opcao == '6':
            u.limparTela()
            relatorioMensal()

        elif opcao == '7':
            u.limparTela()
            relatorioAnual()

        elif opcao == '8':
            u.limparTela()
            break
        else:
            u.limparTela()
            print('Opcão Inválida')
            u.readKey()

if __name__ == '__main__':
    menuRelatorio()



#Campos: Data, Descrição, Categoria, Valor