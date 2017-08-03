import os

class Handler(object):
    def __init__(self):
        input_dict = {}
        #add to dict
    def handle_welcome(self):
        command = 'clear'
        if os.name == 'nt':
            command = 'cls'
        os.system(command)
        print("Welcome to Low Power Console v1.03 LTS")
        print()
        print("second message part goes here")
    def _default(self, inputs):
        print("default message stuff goes here")
    def handle_input(self, input):
        if input == "game_over_xxx":
             return False
        input_split = input.split()
        function = input_dict.get(input_split[0], self._default)
        function(input_split[1:])
        return True
