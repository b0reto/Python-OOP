class ExercisePlan:
    id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    @staticmethod
    def get_next_id():
        ExercisePlan.id += 1
        next_id = ExercisePlan.id + 1
        return next_id


    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours)

    def __repr__(self):
        #seld.id??
        return f"Plan <{self.id}> with duration {self.duration} minutes"