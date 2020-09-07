class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    brenda = Pessoa(nome='Brenda', idade=26)
    ricardo = Pessoa(brenda,nome='Ricardo', idade=48)
    print(ricardo.cumprimentar())
    print(ricardo.nome)
    print(ricardo.idade)
    for filho in ricardo.filhos:
        print(filho.nome)
        print(filho.idade)
