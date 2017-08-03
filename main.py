#!/usr/bin/env python3
import sys
from handler import *

def main():
    handler = Handler()
    print(handler.welcome_message)
    still_running = True
    while (still_running):
        #get actual input
        input = "game_over_xxx"
        still_running = handler.handle_input(input)

if __name__ == "__main__":
    main()
sys.exit()
