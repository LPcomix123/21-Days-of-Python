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
mode = "6"

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
        menu_options = ["1. 🎲 Dice Roller", "2. 🪙  Coin Flip", "3. ⏳ Countdown", "4. 🎱 Magic 8 Ball", "5. 📱 Calculator", "6. 🔢 Number Guesser", "7. 📊 Text Stats", " ", "8. ℹ️  About", "0. ❌ Exit"]
        for item in menu_options:
            qtype(item)
            print("")
        type("Option number: ")
        mode = input()
    elif mode == "nmenu" or mode == "": # Not Animated Menu
        clear()
        print("21 Days of Python")
        print("Please select an option to continue:")
        menu_options = ["1. 🎲 Dice Roller", "2. 🪙  Coin Flip", "3. ⏳ Countdown", "4. 🎱 Magic 8 Ball", "5. 📱 Calculator", "6. 🔢 Number Guesser", "7. 📊 Text Stats", " ", "8. ℹ️  About", "0. ❌ Exit"]
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
    elif mode == "4" or mode == "5" or mode == "7": # Feature Under Development
        clear()
        qtype("Feature " + mode + " is currently under development. Please check back later.")
        slp(1)
        mode = "nmenu"
    elif mode == "2": # Coin Flip
        clear()
        type("🪙  Coin Flip")
        print(" ")
        print(" ")
        qtype("Press Enter to flip the coin, or type 'exit' to return to the menu. ")
        flip = input()
        clear()
        print("🪙  Coin Flip")
        print(" ")
        if flip == "":
            cresult = random.choice(["Heads", "Tails"])
            sstype("...")
            clear()
            print("🪙  Coin Flip")
            print(" ")
            qtype("Your Coin Landed on: " + cresult)
            slp(2)
            mode = "nmenu"
        elif flip == "exit":
            mode = "nmenu"
        else:
            clear()
            qtype("Invalid option. Please try again.")
            slp(1)
            mode = "2"
    elif mode == "1": # Dice Roller
        clear()
        type("🎲  Dice Roll")
        print(" ")
        print(" ")
        qtype("Press Enter to roll the dice, or type 'exit' to return to the menu. ")
        roll = input()
        if roll == "":
            dresult = random.randrange(1, 7)
            clear()
            print("🎲  Dice Roll")
            print(" ")
            if dresult == 1:
                dresult = "\033[1m" + "1 ⚀ " + "\033[0m"
            elif dresult == 2:
                dresult = "\033[1m" + "2 ⚁ " + "\033[0m"
            elif dresult == 3:
                dresult = "\033[1m" + "3 ⚂ " + "\033[0m"
            elif dresult == 4:
                dresult = "\033[1m" + "4 ⚃ " + "\033[0m"
            elif dresult == 5:
                dresult = "\033[1m" + "5 ⚄ " + "\033[0m"
            elif dresult == 6:
                dresult = "\033[1m" + "6 ⚅ " + "\033[0m"
            sstype("...")
            clear()
            print("🎲  Dice Roll")
            print(" ")
            qtype("You rolled a: " + str(dresult))
            slp(2)
            mode = "nmenu"
        elif roll == "exit":
            mode = "nmenu"
        else:
            clear()
            qtype("Invalid option. Please try again.")
            slp(1)
            mode = "1"
    elif mode == "3": # Countdown
        clear()
        type("⏳  Countdown")
        print(" ")
        print(" ")
        qtype("Enter a whole number of seconds to count down from or 'exit' to return to the menu: ")
        countdown = input()
        if countdown.isdigit():
            for i in range(int(countdown), 0, -1):
                clear()
                print("⏳  Countdown")
                print(" ")
                print(i)
                slp(1)
            clear()
            print("⏳  Countdown")
            print(" ")
            print("0")
            slp(1)
            clear()
            print("⏳  Countdown")
            print(" ")
            qtype("Times up!")
            slp(1.5)
            mode = "nmenu"
        elif countdown == "exit":
            mode = "nmenu"
        else:
            clear()
            qtype("Invalid input. Please enter a whole number.")
            slp(1)        
    elif mode == "6": # Number Guesser
        clear()
        type("🔢  Number Guesser")
        print(" ")
        print(" ")
        qtype("Select a difficulty level:")
        print(" ")
        qtype("1. 🟢 Easy (1-10)")
        print(" ")
        qtype("2. 🟡 Medium (1-50)")
        print(" ")
        qtype("3. 🔴 Hard (1-100)")
        print(" ")
        qtype("4. 🟣 Extreme (1-1000)")
        print(" ")
        qtype("5. ⚪ UNLIMITED (1-♾️ )")
        print(" ")
        level = input("Option number: ") 
        if level == "1":
            difficulty = "🟢 Easy (1-10)"
            ran = "(1-10)"
            num = random.randrange(1, 11)
            max = 10
        elif level == "2":
            difficulty = "🟡 Medium (1-50)"
            ran = "(1-50)"
            num = random.randrange(1, 51)
            max = 50
        elif level == "3":
            difficulty = "🔴 Hard (1-100)"
            ran = "(1-100)"
            num = random.randrange(1, 101)
            max = 100
        elif level == "4":
            difficulty = "🟣 Extreme (1-1000)"
            ran = "(1-1000)"
            num = random.randrange(1, 1001)
            max = 1000
        elif level == "5":
            difficulty = "⚪ UNLIMITED (1-♾️ )"
            ran = "(1-♾️ )"
            num = random.randrange(1, 99999999999999999999999999999999999)
        else:
            clear()
            qtype("Invalid option. Please try again.")
            slp(1)
            mode = "6"
            difficulty = ""
            num = 0
        clear()
        print("🔢  Number Guesser")
        print(" ")
        type(difficulty)
        print(" ")
        print(" ")
        guesses = 0
        guess = input("Guess a number between " + ran + ": ")
        while guess != str(num):
            guesses += 1
            if guess.isdigit():
                if int(guess) < num:
                    print("Too low! Try again.")
                    slp(0.5)
                    clear()
                    print(difficulty)
                    print(" ")
                    print(" ")
                    guess = input("Guess number " + str(guesses) + ", Guess a number between " + ran + ": ")
                elif int(guess) > num:
                    print("Too high! Try again.")
                    slp(0.5)
                    clear()
                    print(difficulty)
                    print(" ")
                    print(" ")
                    guess = input("Guess number " + str(guesses) + ", Guess a number between " + ran + ": ")
                elif guess == "exit":
                    mode = "nmenu"
                    break
                elif int(guess) >= max:
                    if level != "5":
                        print("Number out of range. Please enter a number between 1 and " + str(max) + ".")
                        slp(1)
                        clear()
                        print(difficulty)
                        print(" ")
                    print(" ")
                    guess = input("Guess number " + str(guesses) + ", Guess a number between " + ran + ": ")
            else:
                print("Invalid input. Please enter a whole number.")
                slp(1)
                clear()
                mode = "6"
        guesses += 1
        clear()
        print("You have guessed", guesses, "times, and the number was", num,)
        slp(2)
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
        type("\033[1m" + "The Answer to the Ultimate Question of Life, the Universe, and Everything" + "\033[0m")
        stype("\033[1m" + "..." + "\033[0m")
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