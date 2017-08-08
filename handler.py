import os

from commands.command import *

class Handler(object):
    def __init__(self):
        self.input_dict = {}
        for command in Command.get_all_commands():
            exec_command = "from commands.{0} import *".format(command)
            exec(exec_command)
            eval_command = "{0}()".format(command.title())
            comm = eval(eval_command)
            self.input_dict[comm.get_key()] = comm.run

    def handle_welcome(self):
        clear_screen = 'tput reset'
        if os.name == 'nt':
            clear_screen = 'cls'
        os.system(clear_screen)
        print("Welcome to Low Power Console v1.03 LTS")
        print()
        print("second message part goes here")
        print()

    def _default(self, inputs):
        print("For a list of commands, type 'help'.")

    def handle_input(self, input):
        print()
        function = self._default
        inputs = input.split()
        if inputs:
            function = self.input_dict.get(
                inputs[0],
                self._default
            )
        function(inputs[1:])
        print()
        return True
