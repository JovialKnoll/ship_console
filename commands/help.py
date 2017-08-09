from commands.command import *

class Help(Command):
    def run(self, inputs):
        print("commands:")
        for command in self.get_visible_commands():
            print(command)
