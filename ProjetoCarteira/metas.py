import utils as u
import main as m

def criarMeta():
    u.readKey()
    pass
def editarMeta():
    u.readKey()
    pass
def excluirMeta():
    u.readKey()
    pass
def listarMetasPercent():
    u.readKey()
    pass

#Campos: nome, valor alvo, prazo
#Indicadores: percentual concluído e valor restante
#Dar uma sugestão de X por Mês para atingir a Meta
def menuMetas(): 
        u.limparTela()
        print('===============================')
        print('--- METAS ---')
        print('===============================')
        print('1 - CRIAR META')
        print('2 - EDITAR META')
        print('3 - EXCLUIR META')
        print('4 - LISTAR METAS E PORCENTAGEM')
        print('0 - VOLTAR')  
        print('===============================')
        opcao = int(input('Digite a opção desejada: '))
        print('===============================')
        if opcao == '1':
            u.limparTela()
            criarMeta()
        elif opcao == '2':
            u.limparTela()
            editarMeta()
        elif opcao == '3':
            u.limparTela()
            excluirMeta()
        elif opcao == '4':
            u.limparTela()
            listarMetasPercent()
        elif opcao == '0':
            m.mainMenu()
        else:
            u.limparTela()
            print('Opcão Inválida')
            u.readKey()
            menuMetas()

if __name__ == '__main__':
    menuMetas()

