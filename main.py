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

    if mode == "1":
        print("Feature 1 is currently under development. Please check back later.")

    if mode == "2":
        print("Feature 2 is currently under development. Please check back later.")

    if mode == "3": 
        print("Feature 3 is currently under development. Please check back later.")

    if mode == "4":
        print("Feature 4 is currently under development. Please check back later.")

    if mode == "5":
        print("Feature 5 is currently under development. Please check back later.")

    if mode == "6":
        print("Feature 6 is currently under development. Please check back later.")

    if mode == "7":
        type("About this program.")
        slp(0.5)
        print("")
        print("")
        qtype("This is a Python project I'm building for the Stardance Sticky Streaks challenge")
        slp(0.5)
        print("")
        qtype("This project is being built over 21 days, with a new feature being developed every 3 days once I've completed the Foundation")
        slp(0.5)
        print("")
        qtype("Current day: 1")