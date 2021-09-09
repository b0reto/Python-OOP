def start_playing(class_name):
    return class_name.play()


class Children:
    def play(self):
        return "Children are playing"

piano = Children()
start_playing(piano)


class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
start_playing(guitar)

