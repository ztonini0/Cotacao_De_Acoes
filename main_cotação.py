from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

cotacao_variavel = web.DataReader('<--TICKET DA EMPRESA-->', data_source = 'yahoo', start="01-01-2020", end="01-01-2021" )
print(cotacao_variavel)
cotacao_variavel["Adj Close"].plot(figsize=(10,15))
axes = plt.gca()
axes.set_title('Empresa')
axes.set_xlabel('Ano/Mês')
axes.set_ylabel('Valores')
plt.show()