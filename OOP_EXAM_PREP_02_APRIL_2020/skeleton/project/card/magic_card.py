from card.card import Card


class MagicCard(Card):
    def __init__(self, name: str, damage_points: int, health_points: int):
        super().__init__(name, damage_points, health_points)
        self.damage_points = 5
        self.health_points = 80
        self.name = name
