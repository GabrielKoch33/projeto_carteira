import subprocess
import sys
import time
from datetime import date,datetime, timedelta
from categorias import listar_categorias

# variaveis importantes
size = 82

'''FUNÇÕES DE INTERFACE'''
def limpar_tela():
    # Usa o módulo subprocess, recomendado pelas diretrizes atuais do Python
    if sys.platform.startswith("win"):
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def pause():
    time.sleep(1.5)
        
def read_key():
    input("Pressione ENTER para voltar ao menu...")


def double_line():
    print('='*size) 
def line():
    print('-'*size)

def imprime_colunas(ref_modulo):
    
    limpar_tela()
    double_line()
    print(f'LISTA DE {ref_modulo}'.center(size,' '))
    double_line()
    print(f'{"ID":<5}{"VALOR":<15}{"DESCRIÇÃO":<30}{"CATEGORIA":<20}{"DATA":<12}')
    line()

'''FUNÇÕES DE VALIDAÇÃO'''
def ler_opcao_menu(num_max_opcao):
    '''
    ler opção dos menus
    '''
    while True:
        try:
            op = int(input('Digite a opção que deseja acessar: '))

        except Exception as erro:
            print(f'Erro: {erro}')
            continue

        else:
            if op < 0 or op > num_max_opcao:
                print('Escolha uma opção dentre as apresentadas!')
                continue
            else:
                return op
        
def valida_editar_ou_excluir_categoria(lista):
    '''
    requer ser chamada para validar o ID que da entrada que o user informar
    '''
    if len(lista) == 10:
        return 'Categorias padrões não são editáveis/removíveis'
    
    else:
        listar_categorias()
        while True:
            try:
                id_informado = int(input('Digite o ID da categoria que deseja alterar ou excluir: '))

            except:
                print('Escolha uma opção (numérica) válida!')
                continue # roda esse try até que uma entrada válida seja informada

            if id_informado <= 10 or id_informado <= 0:
                return 'Categorias padrões do sistema não são editáveis/removíveis'
            else:
                return id_informado #quando a entrada for validada e não der erro, retorna o id da categoria que o user quer usar

def ler_valida_id ():
    '''força o usuário a digitar um int válido'''
    while True: # valida entrada valida de valores
        try:
            id_entrada = int(input('Digite o ID: '))

        except:
            print('Escolha uma opção (numérica) válida!')
            continue # roda esse try até que uma entrada válida seja informada

        else:
            return id_entrada
        
'''FUNÇÕES DE CONVERSÃO'''
def converte_moeda(valor):

    if valor == '':
        return 'Valores vazios não são permitidos!'
    
    try:
        valor = valor.replace('.', '')
        valor = valor.replace(',', '.')
        valor = float(valor)

    except (ValueError,AttributeError):
        return 'Formato inválido'
    
    if valor <= 0:
        return 'Valores negativos ou nulos não são permitidos!'
    
    return valor

def calcula_dias_totais(ref_inicio,ref_fim):
    periodo = ref_fim - ref_inicio
    dias = periodo.days
    return dias
              
def converte_data():
    entrada = input("Digite a data (apenas números, ex: 25122026): ").strip()

    if len(entrada) == 8 and entrada.isdigit():
        texto_data = f"{entrada[:2]}/{entrada[2:4]}/{entrada[4:]}"
        data_formatada = datetime.strptime(
            texto_data,
            "%d/%m/%Y")
        return data_formatada
        # data agora é um OBJETO DATETIME, não string
    else:
        return False

'''FUNÇÕES DE BUSCA E GERAÇÃO'''  
def encontra_campo_e_indice(ref_valor, ref_lista,campo_alvo):
    '''
    Campo alvo deve existir como key dentro do dicionário
    '''
    for index, item in enumerate(ref_lista):
        if item [campo_alvo] == ref_valor:
            return True, index
    else:  
        return False, -1
    
def gera_id(lista):
    '''
    acessa uma lista, se for vazia retorna id 1 para o 1º elemento, senão encontra o maior nº id e + 1
    '''
    if not lista:
        return 1
    else:
        return max(item["id"] for item in lista) + 1

'''FUNÇÕES DE SALDO'''
def redefine_saldo():
    pass

saldo = ''
saldo_inicial = 0
def calcula_saldo():
    '''
    common cases:
    *Entradas*
    -> add entrada: saldo += valor_entr
    -> exc entrada: saldo -= valor_entr_excluida
    -> upd entrada: 
        -> vl_novo > vl_velho: saldo += (vl_novo - vl_velho)
        -> vl_novo < vl_velho: saldo -= (vl_velho - vl_novo)
    *Saídas*
    -> add saida: saldo -= vl_saida
    -> exc saida: saldo += vl_excl
    -> upd saida: 
        -> vl_novo > vl_velho: saldo -= (vl_novo - vl_velho)
        -> vl_novo < vl_velho: saldo += (vl_velho - vl_novo) 
    *Atualizar Saldo*
        saldo += (ultimo_reg_saldo - saldo_inicial_informado)
        -> sistema vai armazenar o ultimo valor automaticamente
    '''
    pass

'''FUNÇÕES DE MANIPULAÇÃO DE ESTRUTURAS'''
def hash_palavra_desc(ref_id,
                      lista_hash,
                      caso,
                      ref_desc=[],
                      tipo_lista=[],
                      ref_indice=0):
    '''
    caso: Criar/Excluir/Editar
    '''
    match caso:
        case 'adicionar':

            for palavra in ref_desc:
                if palavra not in lista_hash:
                    lista_hash[palavra] = set()
                    lista_hash[palavra].add(ref_id)
                else:
                    lista_hash[palavra].add(ref_id)
    
        case 'excluir':

            for palavra in tipo_lista[ref_indice]['descricao']:
                lista_hash[palavra].discard(ref_id)
                if not lista_hash[palavra]:
                    del lista_hash[palavra]
            
        case 'editar':
            
            for palavra in tipo_lista[ref_indice]['descricao']:
                lista_hash[palavra].discard(ref_id)
                if not lista_hash[palavra]:
                    del lista_hash[palavra]
                
            for palavra in ref_desc:
                if palavra not in lista_hash:
                    lista_hash[palavra] = set()
                    lista_hash[palavra].add(ref_id)
                else:
                    lista_hash[palavra].add(ref_id)

            tipo_lista[ref_indice]['descricao'] = ref_desc


'''
cria
                for palavra in descricao_entrada: # como descrição é uma lista, cada palavra vai ser uma chave em um dicionario
                    if palavra not in est.palavras_desc_entradas:
                        est.palavras_desc_entradas[palavra] = set()
                        est.palavras_desc_entradas[palavra].add(id)
                    else: # cada palavra vai conter um set onde guarda os ID das entradas
                        est.palavras_desc_entradas[palavra].add(id)
'''
'''
exc

            for item in est.lista_entradas[indice]['descricao']:
                est.palavras_desc_entradas[item].discard(id_removido)
                if not est.palavras_desc_entradas[item]: # se o set ficou vazio (a palavra (key) so aparecia nesse log) então exclui a key
                    del est.palavras_desc_entradas[item]
'''
'''
edit
                        for item in est.lista_entradas[indice]['descricao']:
                            est.palavras_desc_entradas[item].discard(id_entrada)
                            if not est.palavras_desc_entradas[item]:
                                del est.palavras_desc_entradas[item] 
                        
                        # loop para criar a hash das palavras da nova descrição
                        for item in nova_descricao:
                            if item not in est.palavras_desc_entradas:
                                est.palavras_desc_entradas[item] = set()
                                est.palavras_desc_entradas[item].add(id_entrada)
                            else: # cada palavra vai conter um set onde guarda os ID das entradas
                                est.palavras_desc_entradas[palavra].add(id)
'''