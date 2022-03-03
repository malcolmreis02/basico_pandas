import pandas as pd

tabela = pd.read_excel('./Vendas.xlsx')

#após obter os dados da tabela, ver um panorama geral desses dados, no caso das vendas, isso se refere ao faturamento da empresa, faturamento de cada loja, faturamento de cada produto, etc

faturamento_total = tabela['Valor Final'].sum()



faturamento_por_loja = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()   
#ver qual loja vendeu mais, qual produto foi mais vendido, etc               
#pegar as colunas que são mais relevantes para essa analise, tirar as outras, agrupar as lojas em uma linha só somando os valores finais de cada loja

faturamento_por_produto = tabela[['ID Loja', 'Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum()
#vai me retornar o faturamento de cada produto referente a cada loja para analisarmos qual produto está vendendo mais em umas lojas e menos em outras


print(faturamento_por_produto)