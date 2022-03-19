carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 10))
carrinho.append(('produto 4', 60))

soma = sum([v for p, v in carrinho])
print(soma)
