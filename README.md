# Fatoração QR

Quando se trabalha com matrizes, é frequente a dificuldade de se resolver problemas quando as matrizes são cheias (ou bastante recheadas, pelo menos), gerando problemas tanto teóricos quanto técnicos. As fatorações oferecem matrizes alternativas mais simples para esses casos, e uma delas é conhecida como <i>Fatoração QR</i>.

Na fatoração QR, uma matriz $A$ é repartida em duas outras matrizes: $Q$, uma matriz ortogonal, e $R$, uma matriz triangular superior. As propriedades oferecidas por esses dois tipos de matrizes podem ser bastante úteis em muitos casos, como na aproximação de retas via Mínimos Quadrados, por exemplo.

O programa contido neste repositório objetiva oferecer as matrizes $Q$ e $R$ se utilizando de três métodos diferentes: Gram-Schmidt Clássico, Gram-Schmidt Modificado e Reflexões de Householder. As referências utilizadas e o relatório deste projeto podem ser encontradas em [LINK]. 

Foi feita uma versão Web utilizando <a href="https://pyscript.net/">PyScript</a>, que pode ser acessada <a href="https://potalej.github.io/fatoracao-QR-web/">aqui</a>

## Rodando

Para encontrar as matrizes, basta chamar alguma das funções `GSClassico`, `GSModificado` ou `QR_Householder`, disponíveis em seus respectivos arquivos. Todas recebem como parâmetro uma matriz $A_{m \times n}$ e retornam uma tupla `(Q, R)`, com $Q_{m \times m}$ e $R_{m \times n}$, todas do tipo `MatrizDict`.

Há também disponível uma função que mesura e exibe em tabela os erros obtidos, bastando passar como parâmetros $A$, $Q$, $R$ e as normas matriciais desejadas num formato de dicionário. Por exemplo:
```Python
A = [...]
Q, R = ...

tabelaMargens(A, Q, R, normas={
  "norma 1": func1,
  "norma 2": func2,
  ...
})
```

Serão exibidas as normas $\Vert A-QR \Vert $ e $\Vert I-Q^tQ \Vert $, medindo a precisão da fatoração e a precisão da ortogonalização, respectivamente.

## Matrizes e funções auxiliares

Para trabalhar com matrizes, foi utilizada uma classe disponível <a href="https://github.com/Potalej/Matrizes-Dict">aqui</a>, e no arquivo <i>matrizes_exemplos.py</i> pode-se encontrar alguns geradores de matrizes, como <a href="https://en.wikipedia.org/wiki/Magic_square">quadrados mágicos</a> e <a href="https://en.wikipedia.org/wiki/Hilbert_matrix">matrizes de Hilbert</a>.

Também foi utilizado o cálculo de norma vetorial (norma 2) disponível em <i>normas.py</i>, normas matriciais (p-ésima, infinito e de Frobenius) em <i>normas_matriciais.py</i> e número de condicionamento em <i>condicionamento.py</i>.