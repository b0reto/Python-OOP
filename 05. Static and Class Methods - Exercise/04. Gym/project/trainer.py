class Trainer:
    id = 0

    def __init__(self, name:str):
        self.name = name

    @staticmethod
    def get_next_id():
        Trainer.id += 1
        next_id = Trainer.id + 1
        return next_id


def __repr__(self):
        return f"Trainer <{self.id}> on {self.name}"