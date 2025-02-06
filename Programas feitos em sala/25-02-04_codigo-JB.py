#
#   Codigo para montar grafico de uma ação
#
#       José Bezerra
#            04/02/2025

import yfinance as yf
import mathplotlib.pyplot as plt
from pprint import pprint

#https://rowzero.io/blog/yfinance

ticker = 'PETR4.SA'
df = yf.download(ticker, period'5mo')

dados = df['close'].to_dict()
pprint(dados)

datas = list(dados['PETR4.SA'].keys())

precos = list(dados['PETR4.SA'].values())

#plt.plot(df.index, df["Close"], "purple")


plt.plot(datas,precos, color="purple")

plt.title(f"Historico preços - {ticker}")
plt.xlabel("Data")
plt.ylabel("Preço (R$)")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()