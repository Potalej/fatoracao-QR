from qr_gsclassico import GSClassico
from qr_gsmodificado import GSModificado
from qr_hh import QR_Householder
from auxiliares.erros import tabelaMargens
from exemplos.matrizes_exemplos import magica, hilbert
from time import time
from tabulate import tabulate

divisor = 47*"="
######################################

############## ENTRADAS ##############
print(f"{divisor}\n  FATORAÇÃO QR VIA GRAM-SCHMIDT E HOUSEHOLDER\n{divisor}\n")

tipo = int(input("Entre com o número do tipo de matriz desejada:\n1 - Quadrado Mágico\n2 - Hilbert\n>>> "))

tamanho = int(input("\nAgora, entre com a ordem da matriz:\n>>> "))

if tipo == 1:
  M = magica(tamanho)
elif tipo == 2:
  M = hilbert(tamanho)

######################################

print(f"\n\n-> Matriz original: \n{M}\n")

############# FATORAÇÕES #############

fatoracoes = {
  "Gram-Schmidt Clássico": GSClassico,
  "Gram-Schmidt Modificado": GSModificado,
  "Reflexões de Householder": QR_Householder
}

tempos = { fatoracao: 0 for fatoracao in fatoracoes }

for fatoracao in fatoracoes:
  print(f"{divisor}\n=> {fatoracao}\n{divisor}")
  
  # inicia o cronômetro
  t0 = time()  
  # aplica a fatoração
  Q,R = fatoracoes[fatoracao](M)
  # para o cronômetro e salva o valor
  t = time() - t0
  tempos[fatoracao] = t
  # faz a tabela com margens de erro
  tabelaMargens(M, Q, R)
  
  print(f"{divisor}\n")

####################################################
"""
  Averiguar custos de processamento e de consumo de memória, além do tempo demandado para rodar cada função.
"""
print(f"{divisor}{divisor}\n\n{divisor}\n=> Custos\n{divisor}\n")
# monta a tabela de tempo gasto
tabela = [
  [fatoracao, tempos[fatoracao]] for fatoracao in tempos
]
print(tabulate(
    tabela,
    ["Método", "Tempo (em segundos)"],
    tablefmt="presto"
))