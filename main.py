#!/usr/bin/env python3

import sys

from handler import *

def main():
    handler = Handler()
    handler.handle_welcome()
    still_running = True
    while (still_running):
        user_input = input("> ")
        still_running = handler.handle_input(user_input)
    sys.exit()

if __name__ == "__main__":
    main()
