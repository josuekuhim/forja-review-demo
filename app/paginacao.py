def pagina(itens, numero, tamanho=10):
    inicio = numero * tamanho
    return itens[inicio : inicio + tamanho]


def total_paginas(n_itens, tamanho=10):
    return n_itens // tamanho
