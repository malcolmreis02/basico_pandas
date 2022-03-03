import pandas as pd

tabela = pd.read_csv('./ClientesBanco.csv', encoding='latin1')
#para o codigo ler a tabela e tratar os caracteres especiais tipo acentos ou c-cedilha

tabela = tabela.drop('CLIENTNUM', axis=1)
#para eliminar uma coluna da visualização da tabela, axis=1 significa que é coluna, se fosse linha, seria axis=0

#print(tabela.head(10))                 #para vizualizar as dez primeiras informações

#print(tabela.shape)                     #tras as dimensões da tabela (nlinhas, ncolunas)

#print(tabela.describe())                    #tras alguns parametros sobre as colunas tipo minimo, maximo, a metade, media etc

# nova_tabela_1 = tabela[['Idade', 'Sexo']]       #faz uma nova tabela apenas com as colunas que você deseja visualizar
#print(nova_tabela_1)

# ------------- função .loc --------------#

#print(tabela.loc[1:5])                      #pegar todas as informações das linhas 1 até 5

#nova_tabela_2 = tabela.loc[tabela['Categoria'] == 'Cancelado']  #Pega todas as informações que satisfaçam determinada condição
#nova_tabela_3 = nova_tabela_2[['Categoria','Idade','Educação', 'Valor Transacoes 12m']]
#print(nova_tabela_3)

#tabela['Juros contidos'] = tabela['Valor Transacoes 12m'] * 0.08            #adicionando uma coluna com base em outra
#tabela.loc[:,'Verificado'] = 'S'                                #adicionando uma coluna com valor fixo

print(tabela)

