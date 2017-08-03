class Handler(object):
    welcome_message = "test welcome message"
    def __init__(self):
        input_dict = {}
        #add to dict
    def _default(self):
        print("default text goes here")
    def handle_input(self, input):
        #check for special "end everything" input
        if input == "game_over_xxx":
             return False
        #maybe pass in just first word?
        #pass other words to function?
        function = input_dict.get(input, self._default)
        function()
        return True
