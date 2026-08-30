import random
import os
from time import sleep as slp

def type(text):
    for char in text:
        print(char, end='', flush=True)
        slp(0.075)

def qtype(text):
    for char in text:
        print(char, end='', flush=True)
        slp(0.025)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

isactive = 1
mode = "startup"

while isactive == 1:
    if mode == "startup":
        clear()
        slp(1)
        type("Hello there! :)")
        slp(1)
        print(" ")
        type("Welcome to My 21 Days of Python Challenge!")
        slp(1)
        clear()
        mode = "menu"

    if mode == "menu":
        type("21 Days of Python")
        print("")
        type("Please select an option to continue:")
        print("")
        menu_options = ["1. feature1", "2. feature2", "3. feature3", "4. feature4", "5. feature5", "6. feature6", "7. About", "0. Exit"]
        for item in menu_options:
            qtype(item)
            print("")
        type("Option number: ")
        mode = input()

    if mode == "0":
        clear()
        type("Exiting the program...")
        slp(0.25)
        print("")
        type("Bye Bye! :)")
        slp(1)
        clear()
        isactive = 0