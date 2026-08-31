import random
import os
from time import sleep as slp
from datetime import date

def type(text):
    for char in text:
        print(char, end='', flush=True)
        slp(0.075)

def qtype(text):
    for char in text:
        print(char, end='', flush=True)
        slp(0.025)

def stype(text):
    for char in text:
        print(char, end='', flush=True)
        slp(0.3)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

start_date = date(2026, 8, 30)
today = date.today()
current_day = (today - start_date).days + 1
if current_day > 21:
    current_day = 21
elif current_day < 1:
    current_day = 1
isactive = 1
mode = "startup"

while isactive == 1:
    if mode == "startup":
        clear()
        slp(1)
        type("Hello there! :)")
        slp(1)
        print(" ")
        qtype("Welcome to My 21 Days of Python Challenge!")
        slp(1)
        clear()
        mode = "amenu"
    elif mode == "amenu":
        clear()
        type("21 Days of Python")
        print("")
        type("Please select an option to continue:")
        print("")
        menu_options = ["1. feature1", "2. feature2", "3. feature3", "4. feature4", "5. feature5", "6. feature6", " ", "7. About", "0. Exit"]
        for item in menu_options:
            qtype(item)
            print("")
        type("Option number: ")
        mode = input()
    elif mode == "nmenu" or mode == "":
        clear()
        print("21 Days of Python")
        print("Please select an option to continue:")
        menu_options = ["1. feature1", "2. feature2", "3. feature3", "4. feature4", "5. feature5", "6. feature6", " ", "7. About", "0. Exit"]
        for item in menu_options:
            print(item)
        mode = input("Option number: ")
    elif mode == "0":
        clear()
        qtype("Exiting the program...")
        slp(0.25)
        print("")
        type("Bye Bye! :)")
        slp(1)
        clear()
        isactive = 0
    elif mode == "1" or mode == "2" or mode == "3" or mode == "4" or mode == "5" or mode == "6":
        clear()
        qtype("Feature " + mode + " is currently under development. Please check back later.")
        slp(1)
        mode = "nmenu"
    elif mode == "7":
        clear()
        qtype("About this program:")
        slp(0.5)
        print(" ")
        print(" ")
        qtype("This is a Python project I'm building for the Stardance Sticky Streaks challenge,")
        slp(0.5)
        print(" ")
        print(" ")
        qtype("This project is being built over 21 days, with a new feature being developed every 3 days,")
        slp(0.5)
        print(" ")
        print(" ")
        qtype("Current day: " + str(current_day) + "/21")
        slp(0.5)
        print(" ")
        print(" ")
        qtype("Press Enter to return to the menu")
        mode = input()
        clear()
    elif mode == "42":
        clear()
        qtype("\033[1m" + "The Answer to the Ultimate Question of Life, the Universe, and Everything")
        stype("\033[1m" + "...")
        slp(0.5)
        print("")
        print("")
        print("")
        print("")
        type("\x1B[3m" + "But what is the question?" + "\x1B[0m")
        slp(2)
        clear()
        mode = "nmenu"
    else:
        clear()
        qtype("Invalid option. Please try again.")
        slp(1)
        mode = "nmenu"