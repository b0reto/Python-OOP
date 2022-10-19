from project.rooms.room import Room


class AloneOld(Room):

    def __init__(self, name, pension):
        self.members_count = 1
        self.room_cost = 10
        super().__init__(name, pension, self.members_count)
