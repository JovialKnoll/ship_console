from command import *

class Help(Command):
    def get_key(self):
        return "help"
    def run(self, inputs):
        print("commands:")
        for command in self.get_visible_commands():
            print(command)
