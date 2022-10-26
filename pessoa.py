import random

from pokemon import *

NOMES = ["João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego", "Gerônimo", "Patrícia", "Gary"]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Charmilion"),
    PokemonFogo("Flarin"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Magicarp"),
    PokemonAgua("Squirtle"),
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons, start=1):
                print(f"{index}- {pokemon}")
        else:
            print(f"{self} não tem nenhum pokemon")

    def batalhar(self, pessoa):

        print(f"{self} iniciou uma batalha contra {pessoa}!\n")

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f"{self} ganhou a batalha!\n")
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                     print(f"{pessoa} ganhou a batalha!\n")
                     break
        else:
            print("Essa batalha não pode ocorrer")


    def mostrar_dinheiro(self):
        print(f"Você possui $ {self.dinheiro} em sua conta")

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f"Você ganhou $ {quantidade}")
        self.mostrar_dinheiro()



    def escolher_pokemon(self):
        while True:
            if self.pokemons:
                pokemon_escolhido = random.choice(self.pokemons)
                print(f"{self} escolheu {pokemon_escolhido} \n")
                if pokemon_escolhido.vida <= 0:
                    print("Pokemon ferido! Escolha outro Pokemon")
                else:
                    return pokemon_escolhido
            else:
                print("ERRO: esse jogador não tem nenhum Pokemon para ser escolhido")


class Player(Pessoa):
    tipo = "Players"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} Capturou {pokemon}!")

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu Pokemon: ")
                print("")
                try:
                    escolha = int(escolha)-1
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f"{pokemon_escolhido} eu escolho você!!!!!")
                    return pokemon_escolhido
                except:
                    print("Escolha inválida!")
        else:
            print("ERRO: esse jogador não tem nenhum Pokemon para ser escolhido")

    def exporar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f"Um pokemon selvagem apareceu! {pokemon}")
            print("")

            escolha = input("Deseja capturar? (s/n): ")
            if escolha == "s":
                for i in range(3, 0, -1):
                    rng = random.randint(0, 100) - (pokemon.level / 2)
                    if rng >= random.randint(0, 100):
                        self.capturar(pokemon)
                        break
                    else:
                        print(f"O {pokemon} escapou, você tem mais {i} chances!")
                        if i <= 1:
                            print(f"O {pokemon} fugiu, boa sorte da próxima vez :(")

            else:
               print("Ok, tenha uma boa viagem!")


        else:
            print("Essa exploração não deu em nada")


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)



