import utils as u
import main as m
def adicionarDespesa():
    u.readKey()
    pass
def editarDespesa():
    u.readKey()
    pass
def removerDespesa():
    u.readKey()
    pass
def listarDespesa():
    u.readKey()
    pass
def buscarPorDescricao():
    u.readKey()
    pass
def buscarPorCategoria():
    u.readKey()
    pass
def buscarPorPeriodo():
    u.readKey()
    pass

#Campos: id, Data, Descrição, Categoria, Valor
def menuDespesa():
        u.limparTela()
        print('===============================')
        print('--- DESPESAS ---')
        print('===============================')
        print('1 - ADICIONAR DESPESA')
        print('2 - EDITAR DESPESA')
        print('3 - REMOVER DESPESA')
        print('4 - LISTAR DESPESAS')
        print('5 - BUSCA POR DESCRIÇÃO')
        print('6 - BUSCA POR CATEGORIA')
        print('7 - BUSCA POR PERÍODO')
        print('0 - VOLTAR')
        print('===============================')
        opcao = input('Digite a opção desejada: ')
        print('===============================')
        if opcao == '1':
            u.limparTela()
            adicionarDespesa()
        elif opcao == '2':
            u.limparTela()
            editarDespesa()
        elif opcao == '3':
            u.limparTela()
            removerDespesa()
        elif opcao == '4':
            u.limparTela()
            listarDespesa()
        elif opcao == '5':
            u.limparTela()
            buscarPorDescricao()
        elif opcao == '6':
            u.limparTela()
            buscarPorCategoria()
        elif opcao == '7':
            u.limparTela()
            buscarPorPeriodo()
        elif opcao == '0':
            m.mainMenu()
        else:
            u.limparTela()
            print('Opcão Inválida')
            u.readKey()
            menuDespesa()

if __name__ == '__main__':
    menuDespesa()
'''
{
    "id": 1,
    "descricao": "Mercado",
    "valor": 250.00,
    "categoria": "Alimentação",
    "data": "2026-06-10"
}
'''