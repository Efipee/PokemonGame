import random

class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10


    def __str__(self):
        return f"{self.nome}[{self.vida} ❤] (LV: {self.level})"

    def atacar(self, pokemonAlvo):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemonAlvo.vida -= ataque_efetivo

        print(f"{pokemonAlvo} perdeu {ataque_efetivo} de vida!")

        if pokemonAlvo.vida <= 0:
            print(f"{pokemonAlvo} foi derrotado")
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "Eletrico"

    def atacar(self, pokemonAlvo):
        print(f"{self} lançou um raio do trovão em {pokemonAlvo}")
        return super().atacar(pokemonAlvo)

class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemonAlvo):
        print(f"{self} lançou uma bolo de fogo em {pokemonAlvo}")
        return super().atacar(pokemonAlvo)

class PokemonAgua(Pokemon):
    tipo = "Água"

    def atacar(self, pokemonAlvo):
        print(f"{self} lançou um jato d'água em {pokemonAlvo}")
        return super().atacar(pokemonAlvo)
