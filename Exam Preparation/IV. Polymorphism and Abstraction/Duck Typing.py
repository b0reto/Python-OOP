def start_playing(obj):
    # obj = Guitar class
    return obj.play()


# Test Code
class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))
