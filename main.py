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

def sstype(text):
    for char in text:
        print(char, end='', flush=True)
        slp(1)

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
    if mode == "startup": # Startup Message
        clear()
        slp(1)
        type("Hello there! :)")
        slp(1)
        print(" ")
        qtype("Welcome to My 21 Days of Python Challenge!")
        slp(1)
        clear()
        mode = "amenu"
    elif mode == "amenu": # Animated Menu
        clear()
        type("21 Days of Python")
        print("")
        type("Please select an option to continue:")
        print("")
        menu_options = ["1. Dice Roller", "2. Coin Flip", "3. Countdown", "4. Magic 8 Ball", "5. Calculator", "6. Mini Slot Machine", "7. Text Stats", " ", "8. About", "0. Exit"]
        for item in menu_options:
            qtype(item)
            print("")
        type("Option number: ")
        mode = input()
    elif mode == "nmenu" or mode == "": # Not Animated Menu
        clear()
        print("21 Days of Python")
        print("Please select an option to continue:")
        menu_options = ["1. Dice Roller", "2. Coin Flip", "3. Countdown", "4. Magic 8 Ball", "5. Calculator", "6. Mini Slot Machine", "7. Text Stats", " ", "8. About", "0. Exit"]
        for item in menu_options:
            print(item)
        mode = input("Option number: ")
    elif mode == "0": # Exit
        clear()
        qtype("Exiting the program...")
        slp(0.25)
        print("")
        type("Bye Bye! :)")
        slp(1)
        clear()
        isactive = 0
    elif mode == "1" or mode == "3" or mode == "4" or mode == "5" or mode == "6" or mode == "7": # Feature Under Development
        clear()
        qtype("Feature " + mode + " is currently under development. Please check back later.")
        slp(1)
        mode = "nmenu"
    elif mode == "2": # Coin Flip
        clear()
        result = random.choice(["Heads", "Tails"])
        type("🪙  Coin Flip")
        print(" ")
        print(" ")
        qtype("Press Enter to flip the coin, or type 'exit' to return to the menu. ")
        flip = input()
        clear()
        print("🪙  Coin Flip")
        print(" ")
        if flip == "":
            sstype("...")
            clear()
            print("🪙  Coin Flip")
            print(" ")
            qtype("Your Coin Landed on: " + result)
            slp(2)
        elif flip == "exit":
            mode = "nmenu"
        mode = "nmenu"
    elif mode == "8": # About Section
        clear()
        qtype("About this program:")
        slp(0.5)
        print(" ")
        print(" ")
        qtype("This is a Python project I'm building for the Stardance Sticky Streaks challenge,")
        slp(0.5)
        print(" ")
        print(" ")
        qtype("This project is being built over 21 days, with new features being developed every 3 days,")
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
    elif mode == "42": # Easter Egg
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
    else: # Invalid Option
        clear()
        qtype("Invalid option. Please try again.")
        slp(1)
        mode = "nmenu"