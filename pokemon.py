class Pokemon:

    def __init__(self, especie, level=1, nome=None):

        self.especie = especie
        
        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.level = level

    def __str__(self):
        return "{} ({})".format(self.nome, self.tipo, self.level)
    
    def atacar(self, pokemon):
        print("{} atacou {}". format(self, pokemon))


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou bolas de fogo no {}".format(self, pokemon))


class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print("{} lançou jato de agua no {}".format(self, pokemon)) 


m = PokemonFogo("charmander")
p = PokemonEletrico("pikachu")
a = PokemonAgua("Kloyster")

print(m)
print(p)
print(a)

m.atacar(p)
p.atacar(m)
a.atacar(m)