def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"Achave é (chave) eo valor é (valor)")
    print(type(kwargs))


minha_funcao(nome="João", idade=25, país="Brasil")