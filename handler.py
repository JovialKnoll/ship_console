import os
import importlib

from commands.command import *

class Handler(object):
    def __init__(self):
        self.input_dict = {}
        for command in Command.get_all_commands():
            importlib.import_module('commands.' + command)
            #use exec to add to dict
            print(command)
    def handle_welcome(self):
        clear_screen = 'clear'
        if os.name == 'nt':
            clear_screen = 'cls'
        #os.system(clear_screen)
        print("Welcome to Low Power Console v1.03 LTS")
        print()
        print("second message part goes here")
    def _default(self, inputs):
        print("For a list of commands, type 'help'.")
    def handle_input(self, input):
        if input == "xxx":
             return False
        function = self._default
        inputs = input.split()
        if inputs:
            function = self.input_dict.get(
                inputs[0],
                self._default
            )
        function(inputs[1:])
        return True
