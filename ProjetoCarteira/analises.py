import utils as u
import main as m

def categoriaMaiorConsumo(): 
    u.readKey()
    pass
def mesMaiorGasto(): 
    u.readKey()
    pass
def mesMenorGasto():
    u.readKey()
    pass
def taxaMediaEconomia():
    u.readKey()
    pass
def tendenciaSaldo():
    u.readKey()
    pass


def menuAnalises():
    while True:
        u.limparTela()
        print('===============================')
        print('--- ANÁLISES DO USUÁRIO ---')
        print('===============================')
        print('1 - CATEGORIA QUE MAIS CONSOME ')
        print('2 - MÊS COM MAIOR GASTO')
        print('3 - MÊS COM MENOR GASTO')
        print('4 - TAXA MÉDIA DE ECONOMIA')
        print('5 - TENDÊNCIA DO SALDO')
        print('0 - VOLTAR')
        print('===============================')
        opcao = input('Digite a opção desejada: ')
        print('===============================')
        if opcao == '1':
            u.limparTela()
            categoriaMaiorConsumo()
        elif opcao == '2':
            u.limparTela()
            mesMaiorGasto()
        elif opcao == '3':
            u.limparTela()
            mesMenorGasto()
        elif opcao == '4':
            u.limparTela()
            taxaMediaEconomia()
        elif opcao == '5':
            u.limparTela()
            tendenciaSaldo()
        elif opcao == '0':
            u.limparTela()
            break
        else:
            u.limparTela()
            print('Opcão Inválida')
            u.readKey()

            
if __name__ == '__main__':
    menuAnalises()


