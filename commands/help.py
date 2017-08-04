from command import *

class Help(Command):
    def __init__(self):
        #place non-hidden commands here
        self.command_list = [
            "help"
        ]
    def get_key(self):
        return "help"
    def run(self, inputs):
        print("commands:")
        for command in command_list:
            print(command)
