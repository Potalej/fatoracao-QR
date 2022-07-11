"""
    O número de condicionamento de uma matriz `A` estabelece uma estimativa da precisão que se pode obter para uma solução aproximada de `Ax = b`.
    
    Esse número pode ser obtido antes dos efeitos dos erros de arredondamento (de aritmética de ponto flutuante no geral), pois é uma propriedade da matriz A, não do algoritmo resolutivo ou da máquina que vai resolver o sistema.

    [https://en.wikipedia.org/wiki/Condition_number]
"""
from numpy import matrix
from numpy.linalg import inv, det
from normas_matriciais import norma_Frobenius
from matrizes import MatrizDict

def numCond(A)->float or None:
    """
        A função recebe como parâmetro uma matriz `A` do tipo `MatrizDict`, e o número de condição k(A) é definido por:

            `k(a) := ||A^-1|| * ||A||`
        
        A norma que está sendo utilizada é a de Frobenius.

        Caso `A` seja uma matriz singular, é retornado um erro. A averiguação de sua singularidade é feita através da função `numpy.linalg.det`.

        Para encontrar `A^-1` está sendo utiliza a função `numpy.linalg.inv` para matrizes do tipo `numpy.matrix`.
    """
    # verifica se A é inversível através de sua determinante
    if det(A.lista()) == 0:
        # se for nula, pode parar por aí porque é singular
        raise ValueError("A matriz fornecida é singular!")
    # encontra A^-1
    invA = MatrizDict(inv(matrix(A.lista())))
    # calcula as normas
    norma_A = norma_Frobenius(A)
    norma_invA = norma_Frobenius(invA)
    # retorna o produto das normas
    return norma_invA * norma_A