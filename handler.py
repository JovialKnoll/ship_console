class Handler(object):
    def __init__(self):
        input_dict = {}
        #add to dict
    def default():
        print("default text goes here")
    def handle_input(input):
        #check for special "end everything" input
        #maybe pass in just first word? pass other words to function?
        function = input_dict.get(input, self.default)
        function()
        return True
