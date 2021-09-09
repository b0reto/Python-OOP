from project import pokemon
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        # TODO: self.pokemons = [<project.pokemon.Pokemon object at 0x000000DE7A9E3F70>,
        #  <project.pokemon.Pokemon object at 0x000000DE7A9E3640>]
        for el in self.pokemons:
            if el.name == pokemon_name:
                if pokemon in self.pokemons:
                    self.pokemons.remove(pokemon)
                    return f"You have released {pokemon_name}"
                else:
                    break
            return 'Pokemon is not caught'


    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}" + "\n"
        result += f"Pokemon count {len(self.pokemons)}" + "\n"
        for pokemon in self.pokemons:
            result += "- " + pokemon.pokemon_details() + "\n"

        return result

#
# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# third_pokemon = Pokemon("ABC", 100)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(third_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())


