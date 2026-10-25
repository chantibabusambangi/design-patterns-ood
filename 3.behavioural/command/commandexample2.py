'''
                    <<Command>>
                      Command
                    ----------
                    + execute()
                         ▲
            ┌────────────┴────────────┐
            ▼                         ▼
      PowerOnCommand          VolumeUpCommand
            │                         │
            ▼                         ▼
                   TV (Receiver)

Client ─────► Remote (Invoker)

'''

#receiver
class TV:

    def power_on(self):
        print("TV is ON")

    def power_off(self):
        print("TV is OFF")

    def volume_up(self):
        print("Volume Increased")

    def volume_down(self):
        print("Volume Decreased")

#command interface
from abc import ABC, abstractmethod
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

#Concerete commands
class PowerOnCommand(Command):

    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.power_on()


class PowerOffCommand(Command):

    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.power_off()


class VolumeUpCommand(Command):

    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.volume_up()


class VolumeDownCommand(Command):

    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.volume_down()

#invoker
class RemoteControl:

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

#Client
tv = TV()

power_on = PowerOnCommand(tv)
power_off = PowerOffCommand(tv)
volume_up = VolumeUpCommand(tv)
volume_down = VolumeDownCommand(tv)

remote = RemoteControl()

remote.set_command(power_on)
remote.press_button()

remote.set_command(volume_up)
remote.press_button()

remote.set_command(volume_down)
remote.press_button()

remote.set_command(power_off)
remote.press_button()