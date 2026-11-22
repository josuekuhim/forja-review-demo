def pagina(itens, numero, tamanho=10):
    inicio = (numero - 1) * tamanho
    return itens[inicio : inicio + tamanho]
