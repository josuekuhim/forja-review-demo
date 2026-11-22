def media(valores):
    return sum(valores) / len(valores)


def percentual(parte, total):
    return round(parte / total * 100, 1)


def maior_venda(vendas):
    maior = vendas[0]
    for v in vendas:
        if v["valor"] > maior["valor"]:
            maior = v
    return maior
