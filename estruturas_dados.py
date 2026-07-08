lista_categorias = [ 
  {"id":1,"nome":"alimentação","default":True},
  {"id":2,"nome":"transporte","default":True},
  {"id":3,"nome":"moradia","default":True},
  {"id":4,"nome":"saúde","default":True},
  {"id":5,"nome":"educação","default":True},
  {"id":6,"nome":"lazer","default":True},
  {"id":7,"nome":"parcelas","default":True},
  {"id":8,"nome":"salário","default":True},
  {"id":9,"nome":"investimentos","default":True},
  {"id":10,"nome":"outros","default":True}
]

lista_entradas = [
    # {
    #     "id": 2,
    #     "valor": 120.50,
    #     "descricao": ["mercado", "mensal"],
    #     "categoria": "alimentação",
    #     "data": "06/06/2026"
    # }
]

lista_despesas = [

]

logs = [
    # lista que será populada por cada ocorrência de entrada (1) e saída (0)
    # {TIPO: 1 ; VALOR ; ID_NA_LISTA},
    # a cada novo registro, a função calcula_saldo_atual() será chamada.
    # ela vai analisar o tipo de operação e checar condições para somar ou subtrair
]

'''
Abaixo estão duas Tabelas Hash em que cada palavra fornecida dentro do campo descrição
é armazenada como chave do dicionário, e os valores dentro dos sets{} são os ids
dos registros.
'''
palavras_desc_entradas = {
    # "mercado": {2, 7}, -> a palavra mercado aparece nos registro de id 2 e 7
    # "churrasco": {7}
}

palavras_desc_despesas = {

}

