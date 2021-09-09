from project.room import Room



class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    # TODO
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = [r for r in self.rooms if r.number == room_number][0]
            # [r for r in self.rooms] -> list of objects
            # [r.number -> връща атрибута number на конкретната стая]
            self.guests += people
            result = room.take_room(people)
            if not result:
                self.guests += people
            # опитваме да вземем стаята през метода от класа Room
        except:
            pass

        # i = 0
        # while True:
        #     if room_number == self.rooms[i].number:
        #         if not self.rooms[i].is_taken:
        #             if self.rooms[i].capacity >= people:
        #                 self.rooms[i].is_taken = True
        #                 self.rooms[i].guests += people
        #                 self.guests += people
        #
        #         break
        #     else:
        #         i += 1


    def free_room(self, room_number):
        # i = 0
        # while True:
        #     if room_number == self.rooms[i].number:
        #         if self.rooms[i].is_taken:
        #             self.rooms[i].is_taken = False
        #             self.guests -= self.rooms[i].guests
        #             self.rooms[i].guests = 0
        #         break
        #     else:
        #         i += 1

        room = [r for r in self.rooms if r.number == room_number][0]

        room.free_room()

    def status(self):
        free_rooms = []
        total_taken_rooms = []
        for el in range(len(self.rooms)):
            if not self.rooms[el].is_taken:
                free_rooms.append(self.rooms[el].number)
            else:
                total_taken_rooms.append(self.rooms[el].number)

        res = ""
        res += f"Hotel {self.name} has {self.guests} total guests\n"
        res += f"Free rooms: {', '.join(str(el) for el in free_rooms)}\n"
        res += f"Taken rooms: {', '.join(str(el) for el in total_taken_rooms)}"

        return res
from project.hotel import Hotel
from project.room import Room

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())

