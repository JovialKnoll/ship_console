#!/usr/bin/env python3

import sys

from handler import *

def main():
    #input handling
    full_clear = True
    arguments = sys.argv[1:]
    while len(arguments) > 0:
        if arguments[0] == '-t':
            full_clear = False
        else:
            print("usage: {0} [-t]".format(sys.argv[0]))
            sys.exit()
        arguments = arguments[1:]
    #using the handler
    handler = Handler(full_clear)
    handler.handle_welcome()
    still_running = True
    while (still_running):
        user_input = input("> ")
        still_running = handler.handle_input(user_input)
    #done
    sys.exit()

if __name__ == "__main__":
    main()
