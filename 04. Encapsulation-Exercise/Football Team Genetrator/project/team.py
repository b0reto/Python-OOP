from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player.name in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player.name)
        return f"Player {player.name} joined team {self.__name}"


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    def remove_player(self, player_name: str):
        if player_name in self.__players:
            self.__players.remove(player_name)
            return f"{player_name.__dict__}"
        return f"Player {player_name} not found"
