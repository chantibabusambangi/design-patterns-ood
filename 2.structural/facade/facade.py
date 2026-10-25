#provides simplified interface for a system
#It hides the subsystem's internal complexity, allowing clients to perform complex operations through a simple API.
#consists of substsem, facade, client
#subsystem classes
class DVDPlayer:

    def on(self):
        print("DVD Player ON")

    def play(self):
        print("Playing movie")


class Projector:

    def on(self):
        print("Projector ON")


class Amplifier:

    def on(self):
        print("Amplifier ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")


class Lights:

    def dim(self):
        print("Lights dimmed")


class Screen:

    def down(self):
        print("Screen lowered")

#facade
class HomeTheaterFacade:

    def __init__(self, dvd, projector, amplifier, lights, screen):
        self.dvd = dvd
        self.projector = projector
        self.amplifier = amplifier
        self.lights = lights
        self.screen = screen

    def watch_movie(self):
        print("Starting movie...\n")

        self.lights.dim()
        self.screen.down()
        self.projector.on()
        self.amplifier.on()
        self.amplifier.set_volume(20)
        self.dvd.on()
        self.dvd.play()

#client

dvd = DVDPlayer()
projector = Projector()
amplifier = Amplifier()
lights = Lights()
screen = Screen()

home_theater = HomeTheaterFacade(
    dvd,
    projector,
    amplifier,
    lights,
    screen
)

home_theater.watch_movie()