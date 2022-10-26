import pickle

from pokemon import *
from pessoa import *

def escolhe_pokemon_inicial(player):
    print(f"Olá {player}, você poderá escolher agora um Pokemon que irá te acompanhar nessa jornada!")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui 3 escolhas: ")
    print("")
    print("1. Pikachu")
    print("2. Charmander")
    print("3. Squirtle")
    print("")

    while True:
        escolha = input("Escolha seu Pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida!")


def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso")
    except Exception as error:
        print("Erro ao salvar jogo")
        print(error)


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso")
            return player
    except Exception as error:
        print("Save não encontrado")

if __name__ == "__main__":
    print("-------------------------------------------------")
    print("Bem-vindo ao game Pokemon RPG de terminal")
    print("-------------------------------------------------")

    player = carregar_jogo()

    if not player:
        nome = input("Qual o seu nome? ")
        print("")
        player = Player(nome)
        print(f"Olá {player}, esse é um mundo habitado por pokemons, a partir de agora, faz parte da sua missão, se tornar um mestre pokemon!")
        print("Capture o máximo de pokemons que conseguir, e lute com seus inimigos, e como bônus, te darei $ 100!")
        player.mostrar_dinheiro()
        print("")


        if player.pokemons:
            print("")
            print("Já vi que você tem alguns pokemons")
            print("")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokemon, portando precisa escolher seu pokemon inicial")
            print("")
            escolhe_pokemon_inicial(player)
            print("")

        print("Pronto! Agora que você já tem um Pokemon, enfrente seu primeiro inimigo, o Gary!\n")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("-------------------------------------------------")
        print("1. Explorar pelo mundo")
        print("2. Lutar com um inimigo")
        print("3. Ver Pokedex")
        print("0. Sair do jogo")
        print("")
        escolha = input("Sua escolha: ")

        if escolha == "0":
            print("Saindo do jogo...")
            break
        elif escolha == "1":
            player.exporar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        else:
            print("Escolha invalida")